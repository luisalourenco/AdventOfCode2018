
filepath = 'input2.txt' 

x_coords = []
y_coords = []
with open(filepath) as fp: 	
	pcs = fp.readline()
	line = 1
	while pcs:
		pcs = pcs.split("<")
		print "LINE: ",line
		x_vals = pcs[1].split(",")
		y_vals = pcs[2].split(",")

		x = x_vals[0].strip()
		velx = x_vals[1].split(">")[0].strip()

		y = y_vals[0].strip()
		vely = y_vals[1].split(">")[0].strip()

		#print x
		#print velx

		#print y
		#print vely

		x_coords.append(x)
		y_coords.append(y)

		line +=1
		pcs = fp.readline()
	#end while
