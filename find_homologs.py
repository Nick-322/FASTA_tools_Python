#!/usr/bin/env python3

import sys
import os

file1 = sys.argv[1]
file2 = sys.argv[2]
file3 = sys.argv[3]
file4 = sys.argv[4]

unprocessed_file = open(file1, 'r')
contents = unprocessed_file.readlines()
unprocessed_file.close()

#create a list that contains seqid, pident, length, sstart, send, and qlen of the unprocessed BLAST file
new_stuff = []
for line in contents:
    _, blast_seqid, pident, length, _, _, _, _, sstart, send, _, _, qlen = line.strip().split("\t")
    new_stuff.append(f"{blast_seqid}\t{pident}\t{length}\t{sstart}\t{send}\t{qlen}\n")
new_stuff = "".join(new_stuff)

#create a file from the list
blast_out = open("blast_out.txt", 'w') # 'w' mode means we will write to the file
blast_out.write(new_stuff)
blast_out.close()

blast = open("blast_out.txt", 'r')
blast_contents = blast.readlines()
blast.close()

#create a list that contain info of homolog hits with greater than 30% identity and >= 90% length.
out_list=[]
for line in blast_contents:
    blast_seqid, pident, length, sstart, send, qlen = line.strip().split("\t")
    if float(pident) > 30 and int(length) >= int(qlen)*0.9:
        out_list.append(f"{blast_seqid}\t{sstart}\t{send}\n")
homolog_coordinates = "".join(out_list)

#create a homolog file from the list
hlog_file = open("homolog_coordinates.txt", 'w') # 'w' mode means we will write to the file
hlog_file.write(homolog_coordinates)
hlog_file.close()

#open the homolog file
homolog = open("homolog_coordinates.txt", 'r')
homolog_contents = homolog.readlines()
homolog.close()

#open a bedfile
bed = open(file2, 'r')
bed_contents = bed.readlines()
bed.close()

#Find sequence features that contain start/end positions of homolog file & gene names of the matched squence features
gene_list = []
for line1 in homolog_contents:
    blast_seqid, start, end = line1.strip().split("\t")
    for line2 in bed_contents:
        bed_seqid, bed_start, bed_end, gene_name, _, _ = line2.strip().split("\t")
        if blast_seqid != bed_seqid: #skip if the ID between BLAST and BED file don't match
            continue
        if int(start) > int(bed_end): #skip checking the end if we haven't identified the start position of hit yet
            continue
        elif int(start) < int(bed_start): #skip cheking bed start position if we already passed the hit location
            break
        if int(start) > int(bed_start) and int(end) <= int(bed_end):
            gene_list.append(gene_name)

#sort the gene list file
gene_list.sort()


#create a list that has only unique gene name values
unique_homolog = []
for i in gene_list:
    if i not in unique_homolog:
        unique_homolog.append(i)
        #or, I can use set() command like set(gene_list)
        
#count the number of homolog hits
print("the number of homolog hits: " + str(len(unique_homolog)))

#create an list that contains bed info of only unique gene names of the hits
homolog_bed_features = []
for line in bed_contents:
    bed_seqid, bed_start, bed_end, gene_name, _, direction = line.strip().split("\t")
    for i in unique_homolog:
        if i == gene_name:
            feature_data = [bed_seqid, bed_start, bed_end, gene_name, direction]
            homolog_bed_features.append(feature_data)


assembly_file = open(file3, 'r')
assembly_contents = assembly_file.readlines()
#print(assembly_contents[0])
assembly_file.close()


sequence = []
sequence_list = {}
for line in assembly_contents:
    line = line.strip()  # Remove leading/trailing whitespaces
    if line.startswith('>'):
        chrnames = line.split()[0]
        sequence = []
    else :
        sequence.append(line)
    sequence_list[chrnames] = "".join(sequence)


complement_table = {"A":"T", "T":"A", "G":"C", "C":"G"}

#create a list for output file
homolog_sequences = []
for bed_seqid, bed_start, bed_end, gene_name, direction in homolog_bed_features:
    for key in sequence_list:
        if ">"+bed_seqid == key:
            if direction == "-": #reverse complement the sequence and append it to the list with genename
                seq = sequence_list[key][int(bed_start)-1:int(bed_end)]
                reverse_seq = seq[::-1]
                reverse_complement = "".join(complement_table[char] for char in reverse_seq)
                homolog_sequences.append(f">{gene_name}\n{reverse_complement}\n")
            if direction == "+":
                homolog_sequences.append(f">{gene_name}\n{sequence_list[key][int(bed_start)-1:int(bed_end)]}\n")
                
output_data = "".join(homolog_sequences)

output_file = open(f"{file4}.fna", 'w')
output_file.write(output_data)
output_file.close()

#remove temporary files
os.remove("homolog_coordinates.txt")
os.remove("blast_out.txt")


