filepath = 'input.txt' 




with open(filepath) as fp: 	
	input = fp.readline().strip()

	input_pcs = input.split()
	result = 0
	l = input_pcs
	while len(l) > 0:
		children = int(l[0])
		metadata = int(l[1])

		print l
		print "chidlren: ",children
		print "meta: ",metadata

		
		if children == 0: # read metadata from ahead
			#print "base case: ", l
			i = 2
			m = metadata
			while metadata > 0:
				result += int(l[i])
				print "metadata val: ", int(l[i])
				metadata -= 1
				i += 1

			l = l[2+m:]

		else: # read metadata from tail
			i = len(l)-1
			#print "i: ", i
			m = metadata
			while metadata > 0:
				result += int(l[i])
				print "metadata val: ", int(l[i])
				metadata -= 1
				i -= 1

			#print "recursive: ", l[2:len(l)-m]
			l = l[2:len(l)-m]

		#print "result: ",result
	#endwhile
	print "final: ",result



