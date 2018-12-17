import string

filepath = 'input.txt' 

letters = []
polymersSize = []


with open(filepath) as fp: 	
	polymer = fp.readline().strip()
	finalPolymer = [''] * len(polymer)
	original = polymer

	# build list with all existing letters in polymer
	for i in range(0,len(polymer)):
		if not polymer[i].lower() in letters:
			letters.append(polymer[i].lower())
		if len(letters) == 26:
			break
	
	letters.sort()
	for l in letters:
		polymer = original
		reactions = 1
		while reactions > 0:
			reactions = 0
			pos = 0
			skip = False

			for i in range(0, len(polymer)-1):							
				#print(i, ", letter ", l, " ",polymer[i], " ", polymer[i+1] )

				if skip:
					skip = False
				else:
					if polymer[i] == polymer[i+1] or polymer[i].lower() != polymer[i+1].lower():
						#same letter with same case or different letters
						if not polymer[i].lower() == l:
							finalPolymer[pos] = polymer[i]
							pos += 1
					else: #reaction BOOM!
						skip = True
						reactions += 1
			#end for

			finalPolymer[pos] = polymer[i+1]
			polymer = finalPolymer
		#end while	

		#print(finalPolymer)
		size = len(list(filter(lambda x: x != '', finalPolymer)))
		polymersSize.append(size)
		#print(size)
	#end for letters
	print(min(polymersSize))




