with open("C:/Users/dmlam/Desktop/AOC2024 D-6.txt", "r") as file:
    content = file.read()
    lines = content.splitlines()  # This returns a list of lines, with newline characters
map = []
for i in range(len(lines)):
    map.append(list(lines[i]))

def find_starting_point(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "^":
                return [i, j]
position_garde = find_starting_point(map)

def find_obstacle(map):
    obstacles = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "#":
                obstacles.append([i, j])
    return obstacles
position_obstacles = find_obstacle(map)


direction = 0 #direction initale = haut, avec rotation 90d droite pour chaque direction % 4
anciennes_positions =[]
while 0 <= position_garde[0] < 130 and 0 <= position_garde[1] < 130 :
    if direction % 4 == 0:
        if [position_garde[0]-1, position_garde[1]] not in position_obstacles:
            if position_garde not in anciennes_positions:
                anciennes_positions.append(list(position_garde))
            position_garde[0] -= 1
        else :
            direction += 1
    elif direction % 4 == 2:
        if [position_garde[0]+1, position_garde[1]] not in position_obstacles:
            if position_garde not in anciennes_positions:
                anciennes_positions.append(list(position_garde))
            position_garde[0] += 1
        else :
            direction += 1
    elif direction % 4 == 1:
        if [position_garde[0], position_garde[1]+1] not in position_obstacles:
            if position_garde not in anciennes_positions:
                anciennes_positions.append(list(position_garde))
            position_garde[1] += 1
        else :
            direction += 1
    elif direction % 4 == 3:
        if [position_garde[0], position_garde[1]-1] not in position_obstacles:
            if position_garde not in anciennes_positions:
                anciennes_positions.append(list(position_garde))
            position_garde[1] -= 1
        else :
            direction += 1
print(len(anciennes_positions))
#the answer was 5242
