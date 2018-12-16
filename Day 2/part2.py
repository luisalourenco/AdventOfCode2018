filepath = 'input.txt' 
ldict = {}
endLoop = False
with open(filepath) as fp: 	
	boxId = fp.readline().strip()

	while boxId:
		
		# remove each letter from Box ID
		for i in range(len(boxId)):
			start = boxId[0 : (i)] 
			end =  boxId[(i + 1) : len(boxId)]
			#print("0 : ", i-1, " to ", i + 1, " : ", len(boxId) )
			subId = start + end

			if ldict.get(subId) == None:
				ldict[subId] = boxId
			elif ldict.get(subId) != boxId:
				print(subId)
				print(ldict.get(subId))
				print(boxId)
				endLoop = True
				break

		if endLoop:
			break
		boxId = fp.readline().strip()


