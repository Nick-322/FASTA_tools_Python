#!/usr/bin/env python3
import sys
import os
file1 = sys.argv[1]
file2 = sys.argv[2]
file3 = sys.argv[3]

unprocessed_file = open(file1, 'r')
contents = unprocessed_file.readlines()

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
            gene_list.append(f"{gene_name}\n")

#sort the gene list file
gene_list.sort()

#create a list that has only unique gene name values
unique_homolog = []
for i in gene_list:
    if i not in unique_homolog:
        unique_homolog.append(i)
        #or, I can use set() command like set(gene_list)
        
#count the number of homolog hits
print(len(unique_homolog))

#create an output file that contains only unique gene names of the hits
matched_homolog_list = "".join(unique_homolog)
homolog_match = open(file3, 'w')
homolog_match.write(matched_homolog_list)
homolog_match.close()

#remove temporary files
os.remove("homolog_coordinates.txt")
os.remove("blast_out.txt")

