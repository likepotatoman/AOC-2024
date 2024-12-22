with open("AOC2024 D-6 Input.txt", "r") as file:
    content = file.read()
    lines = content.splitlines()  # This returns a list of lines, with newline characters
map = []
for i in range(len(lines)):
    map.append(list(lines[i]))
print(map)

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
print(position_obstacles)


direction = 0 #direction initale = haut, avec rotation 90d droite pour chaque direction % 4
anciennes_positions =[]
while 1 <= position_garde[0] < 128 and 1 <= position_garde[1] < 128 :
    print(position_garde)
    if direction % 4 == 0:
        if [position_garde[0]-1, position_garde[1]] not in position_obstacles:
            anciennes_positions.append(position_garde)
            position_garde[0] -= 1
        else :
            direction += 1
    elif direction % 4 == 2:
        if [position_garde[0]+1, position_garde[1]] not in position_obstacles:
            anciennes_positions.append(position_garde)
            position_garde[0] += 1
        else :
            direction += 1
    elif direction % 4 == 1:
        if [position_garde[0], position_garde[1]+1] not in position_obstacles:
            anciennes_positions.append(position_garde)
            position_garde[1] += 1
        else :
            direction += 1
    elif direction % 4 == 3:
        if [position_garde[0], position_garde[1]-1] not in position_obstacles:
            anciennes_positions.append(position_garde)
            position_garde[1] -= 1
        else :
            direction += 1


print(anciennes_positions)

print(len(anciennes_positions))
#the answer was 
