import re 

r, p = open(0).read().split('\n\n')

registers = []

for l in r.split('\n'):
    registers.append(int(re.findall(r"\d+", l)[0]))

program = list(map(int, re.findall(r"\d+", p)))

def evaluate(program, ans):
    print(program)
    print(ans)
    if program == []:
        return ans
    for i in range(0,8): # since we take last 3 bits, we only search between 0,8
        A = (ans << 3) + i # we had our answer, let's move the 3 bits to the left and try the next 3 bits
        B = A % 8
        B = B ^ 2
        C = A >> B
        B = B ^ C
        B = B ^ 3
        if B % 8 == program[-1]:
            sub_ans = evaluate(program[:-1], A)
            if sub_ans == None:
                continue
            return sub_ans
        
print(evaluate(program, 0))



# 2,4: B = A % 8 take last 3 bits
# 1,2: B = B ^ 2 flips 2nd last bit
# 7,5: C = A >> B take last B bits
# 4,5: B = B ^ C flips last C in binary bits
# 1,3: B = B ^ 3 flips last 2 bits
# 5,5: output = B % 8 take last 3 bits
# 0,3: A = A >> 3 take last 3 bits
# 3,0: jump to 0 if A is not 0