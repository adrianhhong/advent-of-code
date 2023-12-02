import re

# 12 red cubes, 13 green cubes, and 14 blue cubes

total = 0


def is_possible(colour_string):
    if 'red' in colour_string:
        red_num = int(re.findall(r'\d+', colour_string)[0])
        if (red_num > 12):
            return False
    if 'green' in colour_string:
        green_num = int(re.findall(r'\d+', colour_string)[0])
        if (green_num > 13):
            return False
    if 'blue' in colour_string:
        blue_num = int(re.findall(r'\d+', colour_string)[0])
        if (blue_num > 14):
            return False
    return True


with open('input.txt') as input:
    for i, line in enumerate(input):
        line_possible = True
        draws = line.split(':')[1].split(';')
        for draw in draws:
            colour_selection = draw.strip().split(',')
            for colour in colour_selection:
                if not is_possible(colour):
                    line_possible = False
        if line_possible:
            total += (i+1)


print(total)
