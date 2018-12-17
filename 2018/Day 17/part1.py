import sys

x_dict = {}
y_dict = {}
xs = []
ys = []

def flat_list(l):
	flat_list = []
	for sublist in l:
		for item in sublist:
			flat_list.append(item)
	return flat_list


def print_map(m):
	i = 0
	#print "    ",xs
	for s in m:
		print i,": ", s
		i += 1	

def relative_position(x, absolute):
	if x in absolute:
		return absolute.index(x)
	else:
		return -1

def fill_map(m):
	#x 667
	#y 1931

	for y in y_dict.keys():	
		r_y = relative_position(y, ys)

		clays = y_dict.get(y)
		if clays != None:
			for x in clays:
				r_x = relative_position(x, xs)
				#print x, ",", y
				print clays
				m[r_x][r_y] = "#"

	for x in x_dict.keys():
		r_x = relative_position(x, xs)			

		clays = x_dict.get(x)
		if clays != None:
			for y in clays:
				r_y = relative_position(y, ys)
				#print x, ",", y					
				m[r_x][r_y] = "#"
			
def count_tiles(m):
	count = 0
	start_x = relative_position(500, xs)

	print start_x
	for y in range(1,len(ys)):
		if m[start_x][y] != "#":
			count += 1
		
	print count






filepath = 'test.txt' 

with open(filepath) as fp:

	data = fp.readline()	
	
	while data:
		data_pcs = data.split(",")
		one_point = data_pcs[0]
		multiple_points = data_pcs[1]

		# extract data for single point
		one_point_pcs = one_point.split("=")
		coord_s = one_point_pcs[0].strip()
		value_s = int(one_point_pcs[1].strip())

		# extract data for multiple points
		multiple_points_pcs = multiple_points.split("=")
		values_m = [ int(s) for s in multiple_points_pcs[1].split("..") ]
		values_m = range(values_m[0], values_m[1]+1)
	
		# build auxiliary structures
		if coord_s == 'x':
			y_list = x_dict.get(value_s)
			if y_list == None:
				x_dict[value_s] = values_m
			else:
				x_dict[value_s] = y_list + values_m 
		else:
			x_list = y_dict.get(value_s)
			if x_list == None:
				y_dict[value_s] = values_m
			else:
				y_dict[value_s] = x_list + values_m

		data = fp.readline()
	#end while

	aux_x = x_dict.keys() + flat_list(y_dict.values())
	aux_y = y_dict.keys() + flat_list(x_dict.values())

	min_x = min(aux_x)
	min_y = min(aux_y)

	max_x = max(aux_x)
	max_y = max(aux_y)

		

	# order list of Xs nad Ys
	xs = range(min_x-1, max_x+2)
	ys = range(min_y-1, max_y+1)

	columns = len(xs)
	rows =  len(ys)

	# empty map
	#map = [ ['.'] * 1933 for n in range(669)]
	map = [ ['.'] * columns for n in range(rows)]
	map[relative_position(500, xs)][0] = '+'
	
	water_x = xs.index(500) + 1
	water_y = 0
	
	fill_map(map)	

	print_map(map)

	count_tiles(map)

	#print xs
	#print ys

	



