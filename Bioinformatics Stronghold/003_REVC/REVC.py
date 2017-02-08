#!/usr/bin/python

import string

infile = open("rosalind_revc.txt", "r")
outfile = open("output.txt", "w")

DNA = infile.read().strip()
infile.close()

subs = {'A':'T','T':'A','G':'C','C':'G'}

rev = DNA[::-1]

revcom =  "".join([subs[base] for base in rev])

print revcom

outfile.write(revcom)

outfile.close()