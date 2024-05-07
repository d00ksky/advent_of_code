import re

input_file = input("Enter the name of the input file: ")

open_file = open(input_file, "r")
lines = open_file.readlines()

def is_number(x):
    if x in n:
        return str(n.index(x) + 1)  
    return x



sum = 0

n = "one two three four five six seven eight nine".split()

p = "(?=(" + "|".join(n) + "|\\d))"

for x in lines:
    print(x)
    digit = [*map(is_number, re.findall(p, x))]
    print(digit)
    sum += int(digit[0] + digit[-1])

print(sum)
