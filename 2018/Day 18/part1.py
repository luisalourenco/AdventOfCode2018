filepath = 'test.txt' 

def print_map(m):
	i = 0
	for s in m:
		print i,": ", s
		i += 1	


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

	result = [ ['.'] * s for n in range(s)]

	for _ in range(10):
		for i in range(1,s-1):
			for j in range(1,s-1):
				if area[i][j] == "." and countTrees(i, j) >= 3:
					result[i][j] = "|"  
				if area[i][j] == "|" and countLumberyards(i, j) >= 3:
					result[i][j] = "#" 
				if area[i][j] == "#" and countLumberyards(i, j) >= 1 and countTrees(i, j) >= 1:
					result[i][j] = "#"
				else:
					result[i][j] = "."
		#end for
		area = result
	#end for
