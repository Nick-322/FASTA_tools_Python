#!/bin/bash

#file assignment
query="$1"
subject="$2"
output="$3"
    
#perform BLAST with blastn-short task and output format 6 with std + qlen (13 culumns) -> copy only perfect matches to output
blastn -query $query -subject $subject -task blastn-short -outfmt "6 std qlen" | awk '$3 == 100 && $4 == $13' > $output

# Print the number of perfect matches to stdout
echo "Number of perfect matches:"$(wc -l < $output)""

