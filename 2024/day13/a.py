import re
import sympy as sym


input = open(0).read().split('\n\n')

equations = []

t = 0

for i in input:
    line = i.splitlines()
    eq = []
    for l in line:
        eq.append(list(map(int, re.findall(r"\d+", l))))
    button_A, button_B, prize = eq
    A,B = sym.symbols('A,B')
    eq1 = sym.Eq(button_A[0]*A + button_B[0]*B, prize[0])
    eq2 = sym.Eq(button_A[1]*A + button_B[1]*B, prize[1])
    result = sym.solve([eq1,eq2],(A,B))
    if result[A] % 1 == 0 and result[B] % 1 == 0:
        t += result[A]*3 + result[B]

print(t)