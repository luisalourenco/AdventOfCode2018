
filepath = 'input2.txt' 

with open(filepath) as fp: 	
	input = fp.readline().strip()
	
	plants = input
	
	input = fp.readline().strip()
	rules = {}

	# fill rules
	while input:
		plants_pc = input.split('=>')
		input = fp.readline().strip()

		rules[plants_pc[0].strip()] = plants_pc[1].strip()
		
	#print str(rules)

	
	result = ['.'] * (6+len(plants))
	plants = '..' + plants +'...'
	
	for i in range(0,20):
		
		#print "input: ", plants
				
		# check previous generation of plants for this rule
		for pos in range(0, len(plants)):
					
			if pos >= 5:	

				key = plants[pos - 5: pos]

				if rules.get(key) != None:
					val = rules.get(key)										
					result[pos-2] = val					

				#end if rules.get(key)
		
		#endfor pos in range plants

		dots = 3 - (len(result) - "".join(result).rfind("#"))
		for i in range(0, 3):
			result.append('.')

		final = "".join(result) 
		plants = "".join(result)
		result = ['.'] * (len(plants))

	
		print str(i) + ":", final
		#print final.count("#")
	#endfor i in 0 .. 20

	rpos = final.rfind("#") + 1
	lpos = final.find("#")

	final = final[0: rpos]

	print final
	i = -3
	res1 = 0
	for c in final:
		if c == "#":
			res1 += i
		i += 1



	print res1


		
		
