filepath = 'input.txt' 


pos = 0
reactions = 1
with open(filepath) as fp: 	
	polymer = fp.readline().strip()
	finalPolymer = [''] * len(polymer)

	while reactions > 0:
		reactions = 0
		pos = 0
		skip = False
		for i in range(0, len(polymer)-1):
			#print(i, " ",polymer[i], " ", polymer[i+1] )			

			if skip:
				skip = False
			else:
				if polymer[i] == polymer[i+1] or polymer[i].lower() != polymer[i+1].lower():
					#same letter with same case or different letters
					finalPolymer[pos] = polymer[i]
					pos += 1
				else: 
					skip = True
					reactions += 1
				
		finalPolymer[pos] = polymer[i+1]
		polymer = finalPolymer

	#print(finalPolymer)

	print(len(list(filter(lambda x: x != '', finalPolymer))))





