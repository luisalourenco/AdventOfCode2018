import ast

#addr (add register) stores into register C the result of adding register A and register B.
def is_addr(registers, A, B, C, finalRegisters):
	if registers[A] + registers[B]  == finalRegisters[C]:
		return True
	else:
		return False


#addi (add immediate) stores into register C the result of adding register A and value B.
def is_addi(registers, A, B, C, finalRegisters):
	if registers[A] + B  == finalRegisters[C]:
		return True
	else:
		return False


#mulr (multiply register) stores into register C the result of multiplying register A and register B.
def is_mulr(registers, A, B, C, finalRegisters):
	if registers[A] * registers[B]  == finalRegisters[C]:
		return True
	else:
		return False


#muli (multiply immediate) stores into register C the result of multiplying register A and value B.
def is_muli(registers, A, B, C, finalRegisters):
	if registers[A] * B  == finalRegisters[C]:
		return True
	else:
		return False

#banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
def is_banr(registers, A, B, C, finalRegisters):
	if registers[A] & registers[B]  == finalRegisters[C]:
		return True
	else:
		return False

#bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
def is_bani(registers, A, B, C, finalRegisters):
	if registers[A] & B  == finalRegisters[C]:
		return True
	else:
		return False

#borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
def is_borr(registers, A, B, C, finalRegisters):
	if registers[A] | registers[B]  == finalRegisters[C]:
		return True
	else:
		return False

#bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
def is_bori(registers, A, B, C, finalRegisters):
	if registers[A] | B  == finalRegisters[C]:
		return True
	else:
		return False


#setr (set register) copies the contents of register A into register C. (Input B is ignored.)
def is_setr(registers, A, B, C, finalRegisters):
	if registers[A] == finalRegisters[C]:
		return True
	else:
		return False

#seti (set immediate) stores value A into register C. (Input B is ignored.)
def is_seti(registers, A, B, C, finalRegisters):
	if A == finalRegisters[C]:
		return True
	else:
		return False

#gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
def is_gtir(registers, A, B, C, finalRegisters):
	if (A > registers[B] and finalRegisters[C] == 1) or (A <= registers[B] and finalRegisters[C] == 0):
		return True
	else:
		return False

#gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
def is_gtri(registers, A, B, C, finalRegisters):
	if (registers[A] > B and finalRegisters[C] == 1) or (registers[A] <= B and finalRegisters[C] == 0):
		return True
	else:
		return False


#gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
def is_gtrr(registers, A, B, C, finalRegisters):
	if (registers[A] > registers[B] and finalRegisters[C] == 1) or (registers[A] <= registers[B] and finalRegisters[C] == 0):
		return True
	else:
		return False

#eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
def is_eqir(registers, A, B, C, finalRegisters):
	if (A == registers[B] and finalRegisters[C] == 1) or (A != registers[B] and finalRegisters[C] == 0):
		return True
	else:
		return False


#eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
def is_eqri(registers, A, B, C, finalRegisters):
	if (registers[A] == B and finalRegisters[C] == 1) or (registers[A] != B and finalRegisters[C] == 0):
		return True
	else:
		return False

#eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
def is_eqrr(registers, A, B, C, finalRegisters):
	if (registers[A] == registers[B] and finalRegisters[C] == 1) or (registers[A] != registers[B] and finalRegisters[C] == 0):
		return True
	else:
		return False


filepath = 'input.txt' 
count = 0

operation_codes = {0: 'mulr', 1: 'addr', 2: 'banr', 3: 'eqir', 4: 'muli', 5: 'setr', 6: 'eqri', 7: 'gtri', 8: 'eqrr', 9: 'addi', 10: 'gtir', 11: 'gtrr', 12: 'borr', 13: 'bani', 14: 'seti', 15: 'bori'}
with open(filepath) as fp:

	registers = fp.readline()
	
	while registers:
		registers = registers.split(":")[1].strip()
		registers = ast.literal_eval(registers)

		operation = fp.readline().split()
		A = int(operation[1])
		B = int(operation[2])
		C = int(operation[3])
		op_code = int(operation[0])

		finalRegisters = fp.readline().split(":")[1].strip()
		finalRegisters = ast.literal_eval(finalRegisters)
		#read empty line
		fp.readline().split()

		#print registers
		#print operation
		#print finalRegisters
		ops = 0
		op_str = ""

		if is_addr(registers, A, B, C, finalRegisters):
			print "addr: True"
			op_str = "addr" 
			ops += 1
		if is_addi(registers, A, B, C, finalRegisters):
			print "addi: True"
			op_str = "addi" 
			ops += 1	
		if is_mulr(registers, A, B, C, finalRegisters):
			print "mulr: True"
			op_str = "mulr" 
			ops += 1
		if is_muli(registers, A, B, C, finalRegisters):
			print "muli: True"
			op_str = "muli" 
			ops += 1
		if is_banr(registers, A, B, C, finalRegisters):
			print "banr: True"
			op_str = "banr" 
			ops += 1
		if is_bani(registers, A, B, C, finalRegisters):
			print "bani: True"
			op_str = "bani" 
			ops += 1		
		if is_borr(registers, A, B, C, finalRegisters):
			print "borr: True"
			op_str = "borr" 
			ops += 1		
		if is_bori(registers, A, B, C, finalRegisters):
			print "bori: True"
			op_str = "bori" 
			ops += 1
		if is_setr(registers, A, B, C, finalRegisters):
			print "setr: True"
			op_str = "setr" 
			ops += 1
		if is_seti(registers, A, B, C, finalRegisters):
			print "seti: True"
			op_str = "seti" 
			ops += 1
		if is_gtir(registers, A, B, C, finalRegisters):
			print "gtir: True"
			op_str = "gtir" 
			ops += 1
		if is_gtri(registers, A, B, C, finalRegisters):
			print "gtri: True"
			op_str = "gtri" 
			ops += 1
		if is_gtrr(registers, A, B, C, finalRegisters):
			print "gtrr: True"
			op_str = "gtrr" 
			ops += 1
		if is_eqir(registers, A, B, C, finalRegisters):
			print "eqir: True"
			if op_code == 3:
				op_str = "eqir" 
			ops += 1
		if is_eqri(registers, A, B, C, finalRegisters):
			print "eqri: True"
			op_str = "eqri" 
			ops += 1
		if is_eqrr(registers, A, B, C, finalRegisters):
			print "eqrr: True"
			op_str = "eqrr" 
			ops += 1

		print op_code, " - possible operations: ", ops
		if ops >= 3:
			count += 1

		
		registers = fp.readline()
	#end while
	print "Total samples with 3 or more operations: ", count
	print str(operation_codes)

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

