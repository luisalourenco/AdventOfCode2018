import ast

#addr (add register) stores into register C the result of adding register A and register B.
def addr(registers, A, B, C):
	registers[C] = registers[A] + registers[B]	

#addi (add immediate) stores into register C the result of adding register A and value B.
def addi(registers, A, B, C):
	registers[C] = registers[A] + B	

#mulr (multiply register) stores into register C the result of multiplying register A and register B.
def mulr(registers, A, B, C):
	registers[C] = registers[A] * registers[B]

#muli (multiply immediate) stores into register C the result of multiplying register A and value B.
def muli(registers, A, B, C):
	registers[C] = registers[A] * B

#banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
def banr(registers, A, B, C):
	registers[C] = int(registers[A]) & int(registers[B])

#bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
def bani(registers, A, B, C):
	registers[C] = int(registers[A]) & int(B)

#borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
def borr(registers, A, B, C):
	registers[C] = int(registers[A]) | int(registers[B])

#bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
def bori(registers, A, B, C):
	registers[C] = int(registers[A]) | B

#setr (set register) copies the contents of register A into register C. (Input B is ignored.)
def setr(registers, A, B, C):
	registers[C] = registers[A]

#seti (set immediate) stores value A into register C. (Input B is ignored.)
def seti(registers, A, B, C):
	registers[C] = A

#gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
def gtir(registers, A, B, C):
	if A > registers[B]:
		registers[C] = 1
	else:
		registers[C] = 0

#gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
def gtri(registers, A, B, C):
	if registers[A] > B:
		registers[C] = 1
	else:
		registers[C] = 0

#gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
def gtrr(registers, A, B, C):
	if registers[A] > registers[B]:
		registers[C] = 1
	else:
		registers[C] = 0

#eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
def eqir(registers, A, B, C):
	if A == registers[B]:
		registers[C] = 1
	else:
		registers[C] = 0


#eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
def eqri(registers, A, B, C):
	if registers[A] == B:
		registers[C] = 1
	else:
		registers[C] = 0

#eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
def eqrr(registers, A, B, C):
	if registers[A] == registers[B]:
		registers[C] = 1
	else:
		registers[C] = 0


instructions = {'mulr': mulr, 'addr': addr, 'banr': banr, 'eqir': eqir, 'muli': muli, 'setr':setr, 'eqri':eqri, 'gtri':gtri, 'eqrr':eqrr, 'addi': addi, 'gtir': gtir, 'gtrr': gtrr, 'borr':borr, 'bani': bani, 'seti': seti, 'bori': bori}

filepath = 'input.txt' 
count = 0
registers = [10,0,0,0,0,0] # part 2, change register 0 to value 1
operations = []
with open(filepath) as fp:

	ip_reg  = int(fp.readline().split()[1])
	
	operation = fp.readline()

	while operation:
		
		operation = operation.split()
		operations.append(operation)

		operation = fp.readline()
	#end while

	i = 0
	ip = registers[ip_reg]

	s= 100000
	#for _ in range(s):
	while ip < len(operations):

		#print("before: ",registers)

		operation = operations[ip]

		A = int(operation[1])
		B = int(operation[2])
		C = int(operation[3])

		op_code = operation[0]	

		# before, store ip
		registers[ip_reg] = ip	

		# execute instruction	
		instructions[op_code](registers, A, B, C)
		
		#after, load ip
		ip = registers[ip_reg]
		ip += 1
		i += 1

		print(i, ": ",registers[0])
		#if i > s-15:
			#print(i, ": ",operations[ip])
			#print(i, ": ",registers)
	#end for
	print(ip)
	print(registers)
	print(registers[0])

