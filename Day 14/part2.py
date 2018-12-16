scoreboard = [3, 7]
elf1 = 0
elf2 = 1

#input = '59414'

input = '293801'

recipes = 0
mystr = ""
lenMystr = len(mystr)
lenScore = 2
size = len(input)

while recipes == 0:
	recipeScore = scoreboard[elf1] + scoreboard[elf2]


	for s in str(recipeScore):
		scoreboard.append(int(s))
		mystr = mystr + str(s)
		lenMystr += 1
		lenScore += 1

		compareStr = mystr[lenMystr - size:]

		if compareStr == input:
			recipes = lenScore - size


	elf1 = (elf1 + (1 + scoreboard[elf1])) % lenScore
	elf2 = (elf2 + (1 + scoreboard[elf2])) % lenScore

	#print scoreboard
	#print mystr
	#print elf1
	#print elf2


print recipes
