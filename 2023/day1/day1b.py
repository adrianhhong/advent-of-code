import re


def convert_word_to_digit(word):
    match word:
        case "one":
            return '1'
        case "two":
            return '2'
        case "three":
            return '3'
        case "four":
            return '4'
        case "five":
            return '5'
        case "six":
            return '6'
        case "seven":
            return '7'
        case "eight":
            return '8'
        case "nine":
            return '9'
        case _:
            return word


# matches any digit or number spelt as a word
# the tricky part is that there can be overlaps.
# e.g. twone should be one, and threeight should be eight
# We use the positive lookahead (?=()) to make the positive lookahead to include overlaps
regex_digit = r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))'


total = 0

with open('input.txt') as input:
    for line in input:
        first_digit = re.findall(regex_digit, line)[0]
        last_digit = re.findall(regex_digit, line)[-1]
        total += int(convert_word_to_digit(first_digit) +
                     convert_word_to_digit(last_digit))

print(total)
