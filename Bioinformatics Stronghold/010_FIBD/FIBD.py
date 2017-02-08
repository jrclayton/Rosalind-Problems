#!/usr/bin/python

# This approach will use a loop if else loop to split the relations
# based on the input values of n and m
#def fib(n, m):
#	if n < m:
#	# Use relation A
#		if n == 0:
#			return 0
#		elif n == 1:
#			return 1
#		elif n > 1:
#			return fib(n-1, m) + fib(n-2, m) # result from relation A
#	elif n == m or n == m+1:
#	# Use relation B
#		if n == 0:
#			return 0
#		elif n == 1:
#			return 1
#		elif n > 1:
#			return fib(n-1, m) + fib(n-2, m) - 1 # result from relation B
#	elif n > m + 1:
#	# Use relation C
#		if n == 0:
#			return 0
#		elif n == 1:
#			return 1
#		elif n > 1:
#			return fib(n-1, m) + fib(n-2, m) - fib(n-(m+1), m) # result from relation C

### THE ABOVE ALGORITHM HANGS, I THINK BECAUSE IT RELIES ON RECURSION AND MEMORY ALLOCATION
### IS NOT DONE PROPERLY. JUST A GUESS.
			
#run for n months, rabbits die after m months.
total = [1, 1] #Seed the sequence with the 1 pair, then in their reproductive month.
def fib(n, m):
    count = 2
    while count < n:
        if count < m:
        	#recurrence relation before rabbits start dying (simply fib seq Fn = Fn-2 + Fn-1)
            total.append(total[-2] + total[-1]) 
        elif count == m or count == m+1:
        	#Base cases for subtracting rabbit deaths (1 death in first 2 death gens)
            total.append((total[-2] + total[-1]) - 1)#Fn = Fn-2 + Fn-1 - 1
        else:
        	#Our recurrence relation here is Fn-2 + Fn-1 - Fn-(j+1)
            total.append((total[-2] + total[-1]) - (total[-(m+1)])) 
        count += 1
    return (total[-1])

infile = open("rosalind_fibd.txt", "r")
outfile = open("output.txt", "w")

params = infile.read().strip()
infile.close()

n = int(params.split()[0])
m = int(params.split()[1])

final_number = fib(n, m)

print final_number
	
outfile.write(str(final_number))

outfile.close()