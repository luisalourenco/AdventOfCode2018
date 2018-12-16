scoreboard = [3, 7]
elf1 = 0
elf2 = 1

input = 293801


for i in range(0, input + 10):
	recipeScore = scoreboard[elf1] + scoreboard[elf2]

	for s in str(recipeScore):
		scoreboard.append(int(s))

	elf1 = (elf1 + (1 + scoreboard[elf1])) % len(scoreboard)
	elf2 = (elf2 + (1 + scoreboard[elf2])) % len(scoreboard)

	#print scoreboard

	
	#print elf1
	#print elf2

#print scoreboard

mystr = ""
for s in scoreboard[input:input+10]:
	mystr = mystr + str(s)

print mystr