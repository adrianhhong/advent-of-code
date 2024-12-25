from itertools import permutations
from functools import cache

codes = []

numpad = {
    "9": 2+3j,
    "8": 1+3j,
    "7": 3j,
    "6": 2+2j,
    "5": 1+2j,
    "4": 2j,
    "3": 2+1j,
    "2": 1+1j,
    "1": 1j,
    "0": 1,
    "A": 2
}

@cache
def offset_to_moves(offset):
    moves = ""
    hor = offset.real
    ver = offset.imag
    if hor > 0:
        for _ in range(abs(int(hor))):
            moves += ">"
    if hor < 0:
        for _ in range(abs(int(hor))):
            moves += "<"
    if ver > 0:
        for _ in range(abs(int(ver))):
            moves += "^"
    if ver < 0:
        for _ in range(abs(int(ver))):
            moves += "v"
    moves_perms = list(set([''.join(p) for p in permutations(moves)]))
    return moves_perms


def get_lowest(moves):
    lowest = float("inf")
    keep_moves = []
    for m in moves:
        if len(m) < lowest:
            keep_moves = [m]
            lowest = len(m)
        elif len(m) == lowest:
            keep_moves.append(m)
    return keep_moves

directions = {
    ">": 1,
    "v": -1j,
    "<": -1,
    "^": 1j
}

def get_valid_moves_no_gap(moves, start, pad):
    gap = 0
    if pad == numpad:
        gap = 0
    elif pad == keypad:
        gap = 1j
    valid_moves = []
    for m in moves:
        valid = True
        pos = start
        for d in m:
            pos += directions[d]
            if pos == gap:
                valid = False
                break
        if valid:
            valid_moves.append(m)
    return valid_moves


def sequence(l, pad):
    pos = pad["A"]
    possible_moves = [""]
    for v in l:
        offset = pad[v] - pos
        newest_moves = get_valid_moves_no_gap(offset_to_moves(offset), pos, pad)
        newest_possible_moves = []
        lowest = float("Inf")
        for p in possible_moves:
            for n in newest_moves:
                curr_move = p + n + "A"
                if len(curr_move) < lowest:
                    newest_possible_moves = [curr_move]
                    lowest = len(curr_move)
                elif len(curr_move) == lowest:
                    newest_possible_moves.append(curr_move)
        possible_moves = newest_possible_moves
        pos = pad[v]
    return possible_moves



keypad = {
    "A": 2+1j,
    "^": 1+1j,
    ">": 2,
    "v": 1,
    "<": 0
}

t = 0

for l in open(0).read().splitlines():
    s1 = sequence(l, numpad)
    s1 = get_lowest(s1)
    s2 = []
    for s in s1:
        s2 += sequence(s, keypad)
    s2 = get_lowest(s2)
    s3 = []
    for s in s2:
        s3 += sequence(s, keypad)
    s3 = get_lowest(s3)
    lowest = min(len(i) for i in s3)
    print(lowest)
    numeric_code = int(l[:-1])
    t += lowest * numeric_code

print(t)
