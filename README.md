# Python tools for FASTA file editing and analysis
This respository contains...

## Tools this repository contains...

### identify_match.py 
This Python script reads the FASTA file (contains a pair of sequences) and prints the file's sequences to
the terminal along with pipe symbols ("|"), indicating which positions matched. 

Sample output:
Given the following sequences in a FASTA file,

```
>seq1
ATGCAAGTCGAGCGGATGAAGGGAGCTTGCTCCTGGATTCAGCGGCGGAC
>seq2
ATGCAAGTCGAGCGGCAGCACAGAGGAACCTTGGGTGGCGAGCGGCGGAC
```

Your script should produce the output

```
ATGCAAGTCGAGCGGATGAAGGGAGCTTGCTCCTGGATTCAGCGGCGGAC
||||||||||||||| | | ||| || | ||||||||||
ATGCAAGTCGAGCGGCAGCACAGAGGAACCTTGGGTGGCGAGCGGCGGAC
```

Synopsis:
    
    ./identify_match.py <FASTA file>

### homolog_identify.py
homolog_identify.py is a Python alternative of homolog_identify.sh from FASTA-tools that performs the following:

1. Identify putative homologous domains (= homologs) of query amino acid sequences in FASTA format.
2. Use loops & conditional statements to identify which genes in a BED file contain the identified homologs.
3. Write an output file containing the unique gene names (from a given BED file) which your script identified as containing predicted domains.

Synopsis: 

    ./homolog_identify.py <blast output> <BED file> <output file>


### find_homologs.py
find_homologs.py is an extension of homolog_identify.py that has an additional functionality.
The script performs the following tasks:

1. Processe a given BLAST output to keep only hits with >30% identity and 90% length (same as homolog_identify.py)
2. Identify BED features (i.e., genes) that have a BLAST hit entirely within the boundaries of the feature start and end (same as homolog_identify.py)
3. Extract the sequence of identified homologous genes from the assembly sequence
4. If the gene is encoded on the "-" strand in the BED file, reverse & complement the sequence
5. Write the sequences of the homologous genes to the specified output file in FASTA format along with a gene name as header.

        ./find_homologs.py <blast file> <bed file> <assembly file> <output file>
