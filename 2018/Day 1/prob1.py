filepath = 'input.txt' 
freq = 0 
dict = { 0: True }
while True:
	with open(filepath) as fp:  
		line = fp.readline()
		n = 1
		while line:  
			n += 1
			if line != '':
				freq += int(line.strip())
				# check if frequency is repeated
				if dict.get(freq, False) == True:
					print("First repeated: ", freq)
					exit(1)
				else: 
					dict[freq] = True
			line = fp.readline()
		print(freq)