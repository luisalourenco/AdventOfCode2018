filepath = 'input.txt' 

edges = {}
result = ''
with open(filepath) as fp: 	
	tasks = fp.readline().strip()

	while tasks:
		tasks_pcs = tasks.split()
		nodeA = tasks_pcs[1]
		nodeB = tasks_pcs[7]

		if edges.get(nodeA) == None:
			edges[nodeA] = [nodeB]
		else:
			listN = edges.get(nodeA)
			listN.append(nodeB)
			listN.sort()
			edges[nodeA] = listN

		tasks = fp.readline().strip()
	#end while

	flat_list = [item for sublist in edges.values() for item in sublist]
	availablePoints = list(filter(lambda x: x not in flat_list, edges.keys()))

	availablePoints = list(set(availablePoints))
	availablePoints.sort()

	#print(edges)
	#print(availablePoints)
	while len(availablePoints) > 0:
		p = availablePoints.pop(0)
		#print "point ", p
		result += p
		points = edges.get(p)

		#print vals
		if points != None:
			edges.pop(p)
			vals = set([item for sublist in edges.values() for item in sublist])
			for l in points:
				if l not in vals:
					availablePoints.append(l)		
			availablePoints = list(set(availablePoints))
			availablePoints.sort()
		
		#print(availablePoints)

	print(result)





