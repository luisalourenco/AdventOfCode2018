filepath = 'test.txt' 

def print_map(m):
	i = 0
	for s in m:
		print (i,": ", "".join(s))
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
		count =  int(area[i][j+1] == "|") + int(area[i+1][j] == "|") + int(area[i+1][j+1] == "|") + int(area[i-1][j] == "|") + int(area[i-1][j+1] == "|") + int(area[i][j+1] == "|") + int(area[i+1][j] == "|") + int(area[i+1][j+1] == "|")
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
		count =  int(area[i][j+1] == "#") + int(area[i+1][j] == "#") + int(area[i+1][j+1] == "#") + int(area[i-1][j] == "#") + int(area[i-1][j+1] == "#") + int(area[i][j+1] == "#") + int(area[i+1][j] == "#") + int(area[i+1][j+1] == "#")
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
	s = len(data)

	area = [ ['.'] * s for n in range(s)]
	while data:
		area[i] = data
		i += 1
		data = fp.readline().strip()

	print_map(area)
	#print(area[1][6])
	#print(countLumberyards(1,6, area))
	
	result = [ ['.'] * s for n in range(s)]
	for _ in range(10):
	
		for i in range(s):
			for j in range(s):
				#print "checking area ",i,",",j,": ", area[i][j]
				if area[i][j] == "." and countTrees(i, j, area) >= 3:
					#print "Grow Tree!"
					result[i][j] = "|"  
				elif area[i][j] == "|" and countLumberyards(i, j, area) >= 3:
					#print "Become Lumberyard!"
					result[i][j] = "#" 
				elif area[i][j] == "#" and countLumberyards(i, j, area) >= 1 and countTrees(i, j, area) >= 1:
					#print "Remain lumberyard"
					result[i][j] = "#"
				elif area[i][j] == "#" and (countLumberyards(i, j, area) < 1 or countTrees(i, j, area) < 1):
					#print "Become empty!"
					result[i][j] = "."
		#end for
		import copy
		area = copy.deepcopy(result)
		#result = [ ['.'] * s for n in range(s)]
	#end for
	trees = 0
	lumb = 0
	for s in area:
		lumb += s.count("#")
		trees += s.count("|")

	print_map(result)
	print trees
	print lumb
	print trees * lumb

	