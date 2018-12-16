filepath = 'input2.txt' 

edges = {}
result = ''

#times => ord(point)-ord('A') + 1

workers = 2
working = []

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
	totalTime = 0
	#print(edges)
	#print(availablePoints)

	points = []
	while len(availablePoints) > 0:

		#
		print "restart do while, points empty"
		points = []
		while True:

			for w in working:
				if w >= totalTime:
					working.remove(w)
			p = availablePoints.pop(0)
			time = ord(p)-ord('A') + 1 # add 60 for final solution
			working.append(time)
			totalTime += time

			print "point ", p, " will take ", time
			result += p					

			#print "edges: ", edges.get(p)
			for e in edges.get(p):
				points.append(e)
			
			for w in working:
				print w+totalTime, " >= ", totalTime
				if w+totalTime >= totalTime:
					working.remove(w)
			#print points
			if len(working) == workers or len(availablePoints) == 0: 
				break
    	#end while
		print "end while ", len(working)

		print points
		if len(points) != 0:
			edges.pop(p)
			vals = set([item for sublist in edges.values() for item in sublist])
			
			print vals
			for l in points:
				print l, " not in ", vals
				if l not in vals:
					availablePoints.append(l)		
			availablePoints = list(set(availablePoints))
			availablePoints.sort()	
			points = []	
		

		print "available: ",availablePoints

	print(result)
	print totalTime





