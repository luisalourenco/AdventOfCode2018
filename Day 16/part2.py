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
	registers[C] = registers[A] & registers[B]

#bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
def bani(registers, A, B, C):
	registers[C] = registers[A] & B

#borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
def borr(registers, A, B, C):
	registers[C] = registers[A] | registers[B]

#bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
def bori(registers, A, B, C):
	registers[C] = registers[A] | B

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


filepath = 'input2.txt' 
count = 0
registers = [0,0,0,0]
operation_codes = {0: 'mulr', 1: 'addr', 2: 'banr', 3: 'eqir', 4: 'muli', 5: 'setr', 6: 'eqri', 7: 'gtri', 8: 'eqrr', 9: 'addi', 10: 'gtir', 11: 'gtrr', 12: 'borr', 13: 'bani', 14: 'seti', 15: 'bori'}
with open(filepath) as fp:

	operation = fp.readline()
	
	while operation:
		
		operation = operation.split()
		print operation
		A = int(operation[1])
		B = int(operation[2])
		C = int(operation[3])
		op_code = int(operation[0])

		#print operation
	
		if op_code == 1:
			addr(registers, A, B, C)
		if op_code == 0:
			mulr(registers, A, B, C)
		if op_code == 2:
			banr(registers, A, B, C)
		if op_code == 3:
			eqir(registers, A, B, C)
		if op_code == 4:
			muli(registers, A, B, C)
		if op_code == 5:
			setr(registers, A, B, C)
		if op_code == 6:
			eqri(registers, A, B, C)
		if op_code == 7:
			gtri(registers, A, B, C)
		if op_code == 8:
			eqrr(registers, A, B, C)
		if op_code == 9:
			addi(registers, A, B, C)
		if op_code == 10:
			gtir(registers, A, B, C)
		if op_code == 11:
			gtrr(registers, A, B, C)
		if op_code == 12:
			borr(registers, A, B, C)
		if op_code == 13:
			bani(registers, A, B, C)
		if op_code == 14:
			seti(registers, A, B, C)
		if op_code == 15:
			bori(registers, A, B, C)	
	
		operation = fp.readline()
	#end while
	print registers[0]
'''
print "addr: ", is_addr([3, 2, 1, 1], 2, 1, 2,[3, 2, 2, 1])
print "addi: ", is_addi([3, 2, 1, 1], 2, 1, 2,[3, 2, 2, 1])
print "mulr: ", is_mulr([3, 2, 1, 1], 2, 1, 2,[3, 2, 2, 1])
print "muli: ", is_muli([3, 2, 1, 1], 2, 1, 2,[3, 2, 2, 1])
print "banr: ", is_banr([3, 2, 1, 1], 2, 1, 2,[3, 2, 2, 1])
print "bani: ", is_bani([3, 2, 1, 1], 2, 1, 2,[3, 2, 2, 1])
print "borr: ", is_borr([3, 2, 1, 1], 2, 1, 2,[3, 2, 2, 1])
print "bori: ", is_bori([3, 2, 1, 1], 2, 1, 2,[3, 2, 2, 1])
print "setr: ", is_setr([3, 2, 1, 1], 2, 1, 2,[3, 2, 2, 1])
print "seti: ", is_seti([3, 2, 1, 1], 2, 1, 2,[3, 2, 2, 1])
print "gtir: ", is_gtir([3, 2, 1, 1], 2, 1, 2,[3, 2, 2, 1])
print "gtri: ", is_gtri([3, 2, 1, 1], 2, 1, 2,[3, 2, 2, 1])
print "gtrr: ", is_gtrr([3, 2, 1, 1], 2, 1, 2,[3, 2, 2, 1])
print "eqir: ", is_eqir([3, 2, 1, 1], 2, 1, 2,[3, 2, 2, 1])
print "eqri: ", is_eqri([3, 2, 1, 1], 2, 1, 2,[3, 2, 2, 1])
print "eqrr: ", is_eqrr([3, 2, 1, 1], 2, 1, 2,[3, 2, 2, 1])
'''

