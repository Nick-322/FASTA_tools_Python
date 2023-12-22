#!/usr/bin/env python3
import sys
filename = sys.argv[1] #argument assignment
file = open(filename, 'r')
contents = file.readlines()[1:] #read all lines from an fna file and returns them as a list.

#extract and store first and second sequences from the fna file
seq_1 = contents[0].strip()
seq_2 = contents[2].strip()

#create a line of pipes and whitespace to denote the sequence alignment
alignment=[]
for i, n in zip(seq_1, seq_2):
    if i == n:
        alignment.append('|')
    else:
        alignment.append(' ')
alignment_str = "".join(alignment) 

#print pipe symbol between the two sequences at positions where the bases are identical
print(seq_1)
print(alignment_str)
print(seq_2)

#close the input fasta file
file.close()
