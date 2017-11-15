#!/usr/bin/env python
#Reduce function for computing matrix multiply A*B

#Input arguments:
#variable n should be set to the inner dimension of the matrix product (i.e., the number of columns of A/rows of B)

import sys
import string
#import numpy

#number of columns of A/rows of B
n = int(sys.argv[1]) 

#Create data structures to hold the current row/column values (if needed; your code goes here)

list = []

currentkey = None

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

	#Remove leading and trailing whitespace
	line = line.strip().translate(None,"'").translate(None,"{}").replace(':','\t')
	#Get key/value 
	key, values = line.split('\t',1)

	#Parse key/value input (your code goes here)

        key = key.strip()
        values = values.strip().split(" ")
        value = values[2]



	#If we are still on the same key...
	if key==currentkey:

		#Process key/value pair (your code goes here)

                list.append(value)
                list = map(float, list)



	#Otherwise, if this is a new key...
	else:
		#If this is a new key and not the first key we've seen
		if currentkey:

			#compute/output result to STDOUT (your code goes here)
	                
                        alist = list[:len(list)/2]
                        blist = list[len(list)/2:]
                         
                        currentsum = sum([x*y for x, y in zip(alist,blist)])
                        print '(%s),\t%s' % (currentkey, currentsum)
                        

	
		currentkey = key
		
		#Process input for new key (your code goes here)
                
                list = []
                list.append(value)
                list = map(float, list)



#Compute/output result for the last key (your code goes here)

alist = list[:len(list)/2]
blist = list[len(list)/2:]

currentsum = sum([x*y for x, y in zip(alist,blist)])
print '(%s),\t%s' % (currentkey, currentsum)




