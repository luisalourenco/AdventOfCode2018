filepath = 'sort.txt' 

total = 0
mdict = {}
totalTime = {}

with open(filepath) as fp: 	
	entry = fp.readline().strip()
	
	while entry:

		entry_pcs = entry.split()

		date = entry_pcs[0][6:]		
		minutes_str = entry_pcs[1].split(':')[1]
		lenStr = len(minutes_str)

		minutes = int(minutes_str[0: lenStr-1])

		action = entry_pcs[2]

		if action == 'Guard':
			num = int(entry_pcs[3][1:])
			if mdict.get(num) == None:
				mdict[num] = [0] * 60
			if totalTime.get(num) == None:
				totalTime[num] = 0
		elif action == 'falls':
			begin = minutes
		elif action == 'wakes':
			end = minutes
			totalTime[num] += (end-begin)

			for m in range(begin, end):
				mdict.get(num)[m] += 1

	
		entry = fp.readline().strip()

	guardNum = max(totalTime, key=totalTime.get)
	guardMinute = mdict[guardNum].index(max(mdict[guardNum]))

	print("Guard: ", guardNum)
	print("Minute: ", guardMinute)
	print("Value: ", guardNum * guardMinute)




