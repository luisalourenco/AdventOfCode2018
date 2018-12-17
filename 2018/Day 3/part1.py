filepath = 'input.txt' 
map = [['.'] * 1500 for x in range(1500)]
total = 0

with open(filepath) as fp: 	
	claim = fp.readline().strip()
	
	while claim:
		claim_pcs = claim.split()
		num = claim_pcs[0][1:]

		coords = claim_pcs[2].split(',')
		x = int(coords[0])
		y = int(coords[1][0:len(coords[1])-1])

		size = claim_pcs[3].split('x')

		l = int(size[0])
		a = int(size[1])

		for j in range(a):
			for i in range(l):
				if map[y+j][x+i] == '.':
					map[y+j][x+i] = num
				elif map[y+j][x+i] == 'X':
					total += 0
				else:
					map[y+j][x+i] = 'X'
					total += 1

		claim = fp.readline().strip()
	
	print(total)
	#for i in range(10):
	#	print(map[i])
		#print("number: ", num)
		#print("x: ", x)
		#print("y: ", y)
		#print("l: ", l)
		#print("a: ", a)
