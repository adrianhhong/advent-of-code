from itertools import permutations
from functools import cache
import re

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

# get a sequence, find the sequence you need to input in the level above. Split that into sequences separated by "A". Iterate. Find the min of those
@cache
def shortest_sequence(key, depth, pad = keypad):
    if depth == 26:
        return len(key)
    if depth == 0:
        pad = numpad
    seqs = sequence(key, pad)
    optimal = float("Inf")
    for sq in seqs:
        total_for_sq = 0
        split = re.findall(r".+?A", sq)
        for sp in split:
            total_for_sq += shortest_sequence(sp, depth+1)
        optimal = min(optimal, total_for_sq)
    return optimal

t = 0

for l in open(0).read().splitlines():
    lowest = shortest_sequence(l, 0)
    numeric_code = int(l[:-1])
    t += lowest * numeric_code

print(t)
