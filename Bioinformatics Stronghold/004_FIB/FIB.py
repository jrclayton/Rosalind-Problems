#!/usr/bin/python

def fib_rabbits(n, k):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib_rabbits(n-1, k) + k * fib_rabbits(n-2, k)

infile = open("rosalind_fib.txt", "r")
outfile = open("output.txt", "w")

params = infile.read().strip()
infile.close()

n = int(params.split()[0])
k = int(params.split()[1])

final_number = fib_rabbits(n, k)

print final_number
	
outfile.write(str(final_number))

outfile.close()