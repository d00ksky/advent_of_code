input_file = open("test", "r")
lines = input_file.readlines()

grid = [list(line.strip()) for line in lines]

print(grid[1][1])

def is_adjacent_to_a_symbol(grid, x, y):
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if grid[nx][ny] in '*#+$':
                return True
    return False

total_sum = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j].isdigit() and is_adjacent_to_a_symbol(grid, i, j):
            total_sum += int(grid[i][j])

print(total_sum)
