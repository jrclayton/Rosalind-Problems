#!/usr/bin/python

infile = open("rosalind_ini6.txt", "r")
outfile = open("output.txt", "w")

text = infile.read().replace('\n', '')
text = text.replace(', ', '')
#text = text.lower()
text = text.split(' ')

# Generate unique word list
wordlist = []
for i in text:
	if i not in wordlist:
		wordlist.append(i)


# Compare each word in wordlist to each element of text
counts = []
for each in wordlist:
	count = 0
	for j in range(0,len(text)):
		if each == text[j]:
			count += 1
	counts.append(count)

dict = {}

for i in range(0, len(wordlist)):
	dict[wordlist[i]] = counts[i]

for each in dict.keys():
	line = each + " " + str(dict[each]) + "\n"
	outfile.write(line)
	

infile.close()
outfile.close()