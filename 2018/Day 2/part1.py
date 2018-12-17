filepath = 'input.txt' 

twice = 0
thrice = 0
with open(filepath) as fp: 	
	boxId = fp.readline()
	while boxId:
		ldict = {}
		# process all letters of each Box ID
		for c in boxId.strip():
			if  c:
				if ldict.get(c) == None:
					ldict[c] = 1
				else:
					ldict[c] = ldict.get(c) + 1
	
		# check how many Twice or Thrice letters this Box ID has
		# remove duplicates then sort the dictionary values (keys are irrelevant) in descending order 				
		uniqueList = list(dict.fromkeys(ldict.values()))
		uniqueList.sort(reverse=True)
		for count in uniqueList:		
			if count < 2:
				break
			elif count == 2:
				twice += 1
			elif count == 3:
				thrice += 1
		boxId = fp.readline()

print("Twice: ", twice)
print("Thrice: ", thrice)
print("Checksum: ", twice * thrice)

