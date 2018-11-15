#!/bin/bash
cat file.txt | grep -P "^\(\d{3}\) \d{3}-\d{4}$|^\d{3}-\d{3}-\d{4}$"

#I beat 100.0% of bash solutions!
