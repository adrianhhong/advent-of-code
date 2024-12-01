# Python Cheatsheet

https://www.youtube.com/watch?v=NCnHnr9CQ-k

## List and String Manipulation Using (::)

https://www.freecodecamp.org/news/what-does-mean-in-python-operator-meaning-for-double-colon/

General formula
Start is inclusive, stop is non-inclusive

```
collection[start:stop:step]
```

Getting elements from a string

```
chars = "[A] [B] [C]"
print(chars[1:4])
# 'ABC'
```

Reversing a list

```
a = [1, 2, 3]
a[::-1]
# [3, 2, 1]
```

Going backwards, first value should be the end

```
a = [1, 2, 3, 4, 5]
a[3::-2]
# [4, 2]
```

## Sets

Sets are good because there are no duplicates in the set

### Intersection (&)

Common values

```
{1,2,3} & {2,3,4}
# {2, 3}
```

### Union (|)

Values in either set

```
{1,2,3} | {2,3,4}
# {1, 2, 3, 4}
```

### Difference (-)

Values in first set, that are not in the second set

```
{1,2,3} - {2,3,4}
# {1}
```

### Symmetric difference (^)

Values that are in either but not both

```
{1,2,3} ^ {2,3,4}
# {1, 4}
```

### Is Subset (<=)

If every element in first is in second it is a subset

```
{1,2} <= {1,2,3}
# True
```

### Is Proper Subset (<)

If every element in first is in second, and first and second are not the same set, it is a proper subset.

```
{1,2} < {1,2,3}
# True
{1,2} < {1,2}
# False
```

## Reading files

```
open(input.txt).read()
```

Iterating over line in file

```
for l in open(input.txt):
```

## Unpack assignment

```
line = "1 3 4"
x, y, z = map(int, line.split())
# x = 1
# y = 3
# z = 4
```

## Imaginary numbers for coordinates

### Addition and subtraction for offsets

```
x = 2 + 3j
y = 5 + 2j
y - x
# (3-1j)
```

### Rotating clockwise by -90deg

```
(2 + 3j) * -1j
# (3-2j)
```

### Rotating anti-clockwise by 90deg

```
(2 + 3j) * 1j
# (-3+2j)
```

### Rotating by 180deg

```
-(2 + 3j)
# (-2-3j)
```

### Get the final numbers out

```
coord = (2 + 3j)
coord.real
# 2.0
coord.imag
# 3.0
```

## Regular expressions for reading text

```
import re
text = "move 1 object from 2 into 3"
list(map(int, re.findall(r"\d+", text)))
# [1, 2, 3]
```

## Aliases

```
# Advent of Code shortcuts
# Test is in blue, input is in white
# aoca = aota (advent of code test for a.py); aoia (advent of code input for a.py)
alias aota="echo -e '\033[94m'; python3 a.py < test.txt; echo -e '\033[0m'"
alias aoia="python3 a.py < in.txt"
alias aotb="echo -e '\033[94m'; python3 b.py < test.txt; echo -e '\033[0m'"
alias aoib="python3 b.py < in.txt"
alias aoca="aota; aoia"
alias aocb="aotb; aoib"
```
