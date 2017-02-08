#!/usr/bin/python

infile = open("rosalind_dna.txt", "r")
outfile = open("output.txt", "w")

DNA = infile.read()
infile.close()

counts_A = 0
counts_T = 0
counts_C = 0
counts_G = 0

for n in DNA:
    if n == "A":
        counts_A += 1
    elif n == "T":
        counts_T += 1
    elif n == "C":
        counts_C += 1
    elif n == "G":
        counts_G += 1

print "%02d %02d %02d %02d" % (counts_A, counts_C, counts_G, counts_T)

outfile.write("%02d %02d %02d %02d" % (counts_A, counts_C, counts_G, counts_T))

outfile.close()