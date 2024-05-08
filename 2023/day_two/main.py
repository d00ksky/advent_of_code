input_file = open("input", "r")
lines = input_file.readlines()


possible_games = 0

def game_id(line):
    return line.split(" ")[1].strip(':')

def if_possible(game):
    red = 12
    green = 13
    blue = 14
    cubes = game.split(",")
    for cube in cubes:
        cube_color = cube.split()[1]
        cube_num = int(cube.split()[0])
        if cube_color == "red" and cube_num > red:
            return False
        if cube_color == "green" and cube_num > green:
            return False
        if cube_color == "blue" and cube_num > blue:
            return False
    return True

id = 0

for line in lines:
    id = game_id(line)
    impossible_counter = 0
    games = line.split(':', 1)[1].split(';')
    for game in games:
        if if_possible(game) == False:
            impossible_counter += 1
    if impossible_counter == 0:
        possible_games += int(id)

print(possible_games)

