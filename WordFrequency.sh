#!/bin/bash
cat words.txt | tr ' ' $'\n' | sort | sed '/^$/d' | uniq -c | sort -n -r -k2 | awk '{print $2, $1}'

#I beat 100.0% of bash submissions!
