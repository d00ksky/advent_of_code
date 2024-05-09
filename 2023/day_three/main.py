input_file = open("test", "r")
lines = input_file.readlines()

lol = []


# Create grid representation of given data
# searching for each cell if it is digit and if it's a part of bigger number
# searching if that number has adjacent cells with symbols
# marking visited cells and keeping track of them
#
# Building Numbers: When a digit is found, check its adjacent cells to see if they also contain digits. If they do, continue this process recursively, building the number as you go along until no adjacent digits are left. This would help in identifying complete numbers like "467", "35", etc.
# 



# building grid as list of lists:

for line in lines:
    lol.append(line)
print(lol)


for 
