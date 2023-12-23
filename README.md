# Python tools for FASTA 
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
    
    identify_match.py <FASTA file>

### homolog_identify.py


