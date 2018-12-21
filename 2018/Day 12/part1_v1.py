import copy

filepath = 'input.txt' 


cycles = 20
offset = 10

with open(filepath) as fp: 	
	input = fp.readline().strip()
	
	plants = ['.'] * (len(input) + 50)
	size = (len(input) + 50)
	plants[offset:offset + len(input)] = list(input)
	
	print "".join(plants)

	input = fp.readline().strip()
	rules = {}

	# fill rules
	while input:
		plants_pc = input.split('=>')
		input = fp.readline().strip()

		rules[plants_pc[0].strip()] = plants_pc[1].strip()
		
	#print str(rules)

	
	result = ['.'] * (size)
	aux = ['.'] * (size)
	
	for i in range(0,cycles):
		
		#print "input: ", plants
				
		# check previous generation of plants for this rule
		for pos in range(0,  size):
					
			if pos >= 5:	

				key = "".join(plants[pos - 5: pos])

				if rules.get(key) != None:
					val = rules.get(key)										
					result[pos-2] = val	


				#end if rules.get(key)
		
		#endfor pos in range plants
		final =  copy.deepcopy(result)
		plants = copy.deepcopy(result)
		result = copy.deepcopy(aux)

	
		print str(i) + ":", "".join(final)
		
	#endfor i in 0 .. 20


	p = final.index("#")
	final = final[p-3: offset + size]

	print "final: ","".join(final)


	i = -1
	res1 = 0
	for c in final:
		if c == "#":
			res1 += i
		i += 1



	print res1


		
		
