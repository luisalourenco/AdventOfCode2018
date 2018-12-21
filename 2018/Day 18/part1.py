filepath = 'input.txt' 

def print_map(m):
	i = 0
	for s in m:
		#print (i,": ", "".join(s))
		print "".join(s)
		i += 1	

'''
#  #   #
# i,j  #
#  #  #
'''
def countTrees(i, j, area):
	count = 0
	size = len(area[i]) - 1

	if i == 0 and j == size:
		count = int(area[i][j-1] == "|") + int(area[i+1][j-1] == "|") + int(area[i+1][j] == "|") 
	elif i == size and j == 0:
		count = int(area[i-1][j] == "|") + int(area[i-1][j+1] == "|") + int(area[i][j+1] == "|")
	elif i == 0 and j > 0 and j < size:
		count = int(area[i][j-1] == "|") + int(area[i][j+1] == "|")	+ int(area[i+1][j-1] == "|") + int(area[i+1][j] == "|") + int(area[i+1][j+1] == "|")
	elif i == 0 and j == 0 and j < size:
		count = int(area[i][j+1] == "|") + int(area[i+1][j] == "|") + int(area[i+1][j+1] == "|")
	elif i > 0 and j == 0 and i < size:
		count =  int(area[i][j+1] == "|") + int(area[i+1][j] == "|")+ int(area[i+1][j+1] == "|") + int(area[i-1][j] == "|")	+ int(area[i-1][j+1] == "|") 

	elif i == size and j == size:
		count = int(area[i-1][j] == "|") + int(area[i-1][j-1] == "|") + int(area[i][j-1] == "|")
	elif i == size and j < size and j > 0:
		count = int(area[i-1][j] == "|") + int(area[i-1][j-1] == "|") + int(area[i-1][j+1] == "|")+ int(area[i][j-1] == "|") + int(area[i][j+1] == "|")	
	elif j == size and i < size and i > 0:
		count = int(area[i-1][j] == "|") + int(area[i-1][j-1] == "|") + int(area[i][j-1] == "|") + int(area[i+1][j-1] == "|") + int(area[i+1][j] == "|")
	else:
		count = int(area[i-1][j] == "|") + int(area[i-1][j-1] == "|") + int(area[i-1][j+1] == "|")+ int(area[i][j-1] == "|") + int(area[i][j+1] == "|")	+ int(area[i+1][j-1] == "|") + int(area[i+1][j] == "|") + int(area[i+1][j+1] == "|")
	return count


def countLumberyards(i, j, area):	
	count = 0
	size = len(area[i]) - 1
	if i == 0 and j == size:
		count = int(area[i][j-1] == "#") + int(area[i+1][j-1] == "#") + int(area[i+1][j] == "#") 
	elif i == size and j == 0:
		count = int(area[i-1][j] == "#") + int(area[i-1][j+1] == "#") + int(area[i][j+1] == "#")
	elif i == 0 and j > 0 and j < size:
		count = int(area[i][j-1] == "#") + int(area[i][j+1] == "#")	+ int(area[i+1][j-1] == "#") + int(area[i+1][j] == "#") + int(area[i+1][j+1] == "#")
	elif i == 0 and j == 0 and j < size:
		count = int(area[i][j+1] == "#") + int(area[i+1][j] == "#") + int(area[i+1][j+1] == "#")
	elif i > 0 and j == 0 and i < size:
		count =  int(area[i][j+1] == "#") + int(area[i+1][j] == "#") +int(area[i+1][j+1] == "#") + int(area[i-1][j] == "#") +int(area[i-1][j+1] == "#") 
 
	
	elif i == size and j == size:
		count = int(area[i-1][j] == "#") + int(area[i-1][j-1] == "#") + int(area[i][j-1] == "#")
	elif i == size and j < size and j > 0:
		count = int(area[i-1][j] == "#") + int(area[i-1][j-1] == "#") + int(area[i-1][j+1] == "#")+ int(area[i][j-1] == "#") + int(area[i][j+1] == "#")	
	elif j == size and i < size and i > 0:
		count = int(area[i-1][j] == "#") + int(area[i-1][j-1] == "#") + int(area[i][j-1] == "#") + int(area[i+1][j-1] == "#") + int(area[i+1][j] == "#")
	else:
		count = int(area[i-1][j] == "#") + int(area[i-1][j-1] == "#") + int(area[i-1][j+1] == "#")+ int(area[i][j-1] == "#") + int(area[i][j+1] == "#")	+ int(area[i+1][j-1] == "#") + int(area[i+1][j] == "#") + int(area[i+1][j+1] == "#")
	return count


i = 0
with open(filepath) as fp:

	data = fp.readline().strip()	
	s = 50

	area = [ ['.'] * s for n in range(s)]
	result = [ ['.'] * s for n in range(s)]
	while data:
		area[i] = data
		i += 1
		data = fp.readline().strip()

	#print_map(area)
	#print(area[1][6])
	#print(countLumberyards(1,6, area))
	import copy

	part1 = 10
	part2 = 1000000000
	test = 1700



	for p in range(test):
		
		for i in range(s):
			for j in range(s):
				#if area[i][j] == ".":
				#	print "should area ",i,",",j," grow a tree? ", countTrees(i, j, area)
				if area[i][j] == "." and countTrees(i, j, area) >= 3:
					result[i][j] = "|"  

				elif area[i][j] == ".":
					result[i][j] = "."

				elif area[i][j] == "|" and countLumberyards(i, j, area) >= 3:
					result[i][j] = "#" 

				elif area[i][j] == "|":
					result[i][j] = "|"

				elif area[i][j] == "#" and countLumberyards(i, j, area) >= 1 and countTrees(i, j, area) >= 1:
					result[i][j] = "#"
				elif area[i][j] == "#" and (countLumberyards(i, j, area) < 1 or countTrees(i, j, area) < 1):
					result[i][j] = "."
		#end for
		#print "-------", p,"--------"
		#print countTrees(5,0,area)

		#print area[5]
		#print_map(result)

		area = copy.deepcopy(result)
			
		#result = [ ['.'] * s for n in range(s)]
	#end for
	trees = 0
	lumb = 0
	for s in area:
		lumb += s.count("#")
		trees += s.count("|")

	#print "---------------"
	#print_map(result)
	print test
	print trees
	print lumb
	print trees * lumb
	print ""

	