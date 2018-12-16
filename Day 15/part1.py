filepath = "t1.txt"

def computeMap(my_x,my_y,enemy):
	map = []
	x = 0
	for line in map:
		y = 0
		nline = []
		for p in line:
			if p != '#' and p != '.':
				if p == enemy:
					
				#end if p == enemy

			#end p != # and p != .
			y += 1
		#end for p in line
		x += 1
		map.append(nline)
	#end for line in map
	return map

def playGlobin(x,y):
	targets = findTargets(x,y,'E')

	print "Globin (",x,",",y,") plays this round"

def playElf(x,y):
	print "Elf (",x,",",y,") plays this round"


with open(filepath) as fp: 	
	line = fp.readline().strip()

	map = []
	globins = []
	elfs = []
	attack_power = 3

	while line:
		map.append(list(line))

		for l in line:
			if l == 'G':
				globins.append(200)
			if l == 'E':
				elfs.append(200)

		line = fp.readline().strip()
	#end while

	for l in map:
		print "".join(l)

	x = 0
	round = 1
	for line in map:
		y = 0
		
		for p in line:
			if p != '#' and p != '.':
				if p == 'G':
					playGlobin(x,y)
				else: #p == 'E':
					playElf(x,y)
				#end if p == G
			#end p != # and p != .
			y += 1
		#end for p in line
		x += 1
	#end for line in map
