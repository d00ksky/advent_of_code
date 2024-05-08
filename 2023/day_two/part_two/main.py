import re

input_file = open("input", "r")
lines = input_file.readlines()

sum = 0

def game_id(line):
    return line.split(" ")[1].strip(':')

for line in lines:
    id = game_id(line)
    max_numbers = {}
    line = line.split(":")[1].strip("\n")
    cubes = re.split(r'[;,]\s*', line)
    print(id)
    

    for cube in cubes:
        number, color = cube.strip().split()
        number = int(number)
        if color in max_numbers:
            if number > max_numbers[color]:
                max_numbers[color] = number
        else:
            max_numbers[color] = number
    print(max_numbers)
    power = max_numbers["red"] * max_numbers["green"] * max_numbers["blue"]
    print(power)
    sum += power
print(sum)



