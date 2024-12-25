import re 

r, p = open(0).read().split('\n\n')

registers = []

for l in r.split('\n'):
    registers.append(int(re.findall(r"\d+", l)[0]))

program = list(map(int, re.findall(r"\d+", p)))

print(registers)
print(program)

def combo_operand(operand):
    if 0 <= operand <= 3:
        return operand
    elif operand == 4:
        return registers[0]
    elif operand == 5:
        return registers[1]
    elif operand == 6:
        return registers[2]

def opcode_0(operand):
    numerator = registers[0]
    denominator = pow(2, combo_operand(operand))
    registers[0] = numerator // denominator

def opcode_1(operand):
    # bitwise XOR
    registers[1] = registers[1] ^ operand
    
def opcode_2(operand):
    registers[1] = combo_operand(operand) % 8

#check this
def opcode_3(operand):
    if registers[0] == 0: return -1
    return operand

def opcode_4():
    registers[1] = registers[2] ^ registers[1]

def opcode_5(operand):
    return combo_operand(operand) % 8

def opcode_6(operand):
    numerator = registers[0]
    denominator = pow(2, combo_operand(operand))
    registers[1] = numerator // denominator

def opcode_7(operand):
    numerator = registers[0]
    denominator = pow(2, combo_operand(operand))
    registers[2] = numerator // denominator


final = ''
i = 0
while i+1 < len(program):
    print(i)
    print(final)
    opcode = program[i]
    operand = program[i+1]
    if opcode == 0:
        opcode_0(operand)
    elif opcode == 1:
        opcode_1(operand)
    elif opcode == 2:
        opcode_2(operand)
    elif opcode == 3:
        instruct = opcode_3(operand)
        if instruct != -1:
            i = instruct
            continue
    elif opcode == 4:
        opcode_4()
    elif opcode == 5:
        final += str(opcode_5(operand)) + ','
    elif opcode == 6:
        opcode_6(operand)
    elif opcode == 7:
        opcode_7(operand)
    i += 2

print(final)
print(registers)