# read lines and output every other lines

infile = open("rosalind_ini5.txt", "r")
outfile = open("output.txt", "w")

lines = infile.readlines()
for item in lines[1::2]:
	outfile.write("%s" % item)

infile.close()
outfile.close()