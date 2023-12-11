import re

total = 0


def find_num(colour_string):
    return int(re.findall(r'\d+', colour_string)[0])


with open('input.txt') as input:
    for i, line in enumerate(input):
        min_red, min_green, min_blue = 0, 0, 0

        draws = line.split(':')[1].split(';')
        for draw in draws:
            colour_selection = draw.strip().split(',')
            for colour in colour_selection:
                if 'red' in colour:
                    num = find_num(colour)
                    if (num > min_red):
                        min_red = num
                if 'green' in colour:
                    num = find_num(colour)
                    if (num > min_green):
                        min_green = num
                if 'blue' in colour:
                    num = find_num(colour)
                    if (num > min_blue):
                        min_blue = num

        total += min_red * min_green * min_blue


print(total)
