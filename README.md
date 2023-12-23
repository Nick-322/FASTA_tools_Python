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

