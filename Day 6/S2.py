"""
DISCLAIMER : I lost the code for this part and I found it 3 weeks after I had done it to be empty while searching for an algorithm I had written for AOC.
             This was written a second time but I did not run it to check as I have already found the answer with the one at the bottom being the correct one.
"""             

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


def stuck(position_garde, position_obstacles, nouvel_obstacle):
  position_obstacles.append(nouvel_obstacle)
  direction = 0 #direction initale = haut, avec rotation 90d droite pour chaque direction % 4
  anciennes_positions =[]
  
  while 0 <= position_garde[0] < 130 and 0 <= position_garde[1] < 130 :
    if direction % 4 == 0:
        if [position_garde[0]-1, position_garde[1]] not in position_obstacles:
            if [position_garde[0], position_garde[1], direction] not in anciennes_positions:
                anciennes_positions.append(list([position_garde[0], position_garde[1], direction]))
            else :
              return True
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
  return False

total = 0
for i in range(1,len(anciennes_positions)):
  if stuck(position_obstacles, position_garde, anciennes_positions[i]) == True:
    total += 1
print(total)
#the answer was 1424
