#!/bin/bash
if (( $(wc -l < file.txt) >= 10))
then
	head -n 10 file.txt | tail -n 1
fi

#I beat 100.0% of bash submissions!
