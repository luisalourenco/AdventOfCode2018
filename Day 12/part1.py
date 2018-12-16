
filepath = 'input2.txt' 

with open(filepath) as fp: 	
	input = fp.readline().strip()
	
	#plants_l = ['.','.','.']
	#for c in input:
		#plants_l.append(c)

	plants = input
	
	input = fp.readline().strip()
	rules = {}

	# fill rules
	while input:
		plants_pc = input.split('=>')
		input = fp.readline().strip()

		rules[plants_pc[0].strip()] = plants_pc[1].strip()
		

	result = '.' * (6+len(plants))
	plants = '...' + plants +'...'
	
	change = True
	for i in range(0,20):
		
		print plants
		# check each rule
		while (change):
			change = False

			for r in rules.keys():
				val = rules.get(r)

				pos = 0
				plants_pos = 0
				
				# check previous generation of plants for this rule
				for c in plants:
					
					if c == r[pos]:
						pos += 1
					else:
						pos = 0

					if pos == 5:	

						aux = list(result)						
						old_val = aux[plants_pos-2]
						aux[plants_pos-2] = val
						result = "".join(aux)

						if old_val != val:				
							change = True	

						print "PUF! Rule: ", r ," => ", val
						print result
						print "--------"

						break # for c in plants	
					plants_pos += 1			
				#endfor c in plants

			#endfor r in rules
		#end while change
		plants = result

		print str(i) + ":", result
	#endfor i in 0 .. 20
		
		
