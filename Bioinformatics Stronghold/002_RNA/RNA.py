#!/usr/bin/python

infile = open("rosalind_rna.txt", "r")
outfile = open("output.txt", "w")

DNA = infile.read()
infile.close()

RNA = DNA.replace("T", "U")

outfile.write(RNA)

outfile.close()