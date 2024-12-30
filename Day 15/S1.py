with open("C:/Users/dmlam/Desktop/AOC2024 D-15 instructions.txt", "r") as file:
    instructions = file.read()

with open("C:/Users/dmlam/Desktop/AOC2024 D-15 map.txt", "r") as file:
    raw_data = file.read()
    lines = raw_data.splitlines()

warehouse = []
for i in range(len(lines)):
    warehouse.append(list(lines[i]))
position_murs = set()
position_coffres = set()

for i in range(len(warehouse)):
    for j in range(len(warehouse[0])):
        if warehouse[i][j] == "#":
            position_murs.add((i,j))
        elif warehouse[i][j] == "O":
            position_coffres.add((i,j))
        elif warehouse[i][j] == "@":
            position_robot = [i,j]

def execute_instructions(instruction):
    global position_murs, position_coffres, position_robot
    blocs_a_bouger = []
    
    if instruction == "^":
        i = 1
        while (position_robot[0] - i, position_robot[1]) not in  position_murs and (position_robot[0] - i, position_robot[1]) in position_coffres:
            blocs_a_bouger.append((position_robot[0] - i, position_robot[1]))
            i += 1
        if (position_robot[0] - i, position_robot[1]) not in position_murs:
            for index in range(len(blocs_a_bouger) - 1, -1, -1):
                position_coffres.add((blocs_a_bouger[index][0] - 1, blocs_a_bouger[index][1]))
                position_coffres.remove(blocs_a_bouger[index])
            position_robot[0] -= 1
            
    if instruction == "v":
        i = 1
        while (position_robot[0] + i, position_robot[1]) not in  position_murs and (position_robot[0] + i, position_robot[1]) in position_coffres:
            blocs_a_bouger.append((position_robot[0] + i, position_robot[1]))
            i += 1
        if (position_robot[0] + i, position_robot[1]) not in position_murs:
            for index in range(len(blocs_a_bouger) - 1, -1, -1):
                position_coffres.add((blocs_a_bouger[index][0] + 1, blocs_a_bouger[index][1]))
                position_coffres.remove(blocs_a_bouger[index])
            position_robot[0] += 1

    if instruction == ">":
        i = 1
        while (position_robot[0], position_robot[1] + i) not in  position_murs and (position_robot[0], position_robot[1] + i) in position_coffres:
            blocs_a_bouger.append((position_robot[0], position_robot[1] + i))
            i += 1
        if (position_robot[0], position_robot[1] + i) not in position_murs:
            for index in range(len(blocs_a_bouger) - 1, -1, -1):
                position_coffres.add((blocs_a_bouger[index][0], blocs_a_bouger[index][1] + 1))
                position_coffres.remove(blocs_a_bouger[index])
            position_robot[1] += 1

    if instruction == "<":
        i = 1
        while (position_robot[0], position_robot[1] - i) not in  position_murs and (position_robot[0], position_robot[1] - i) in position_coffres:
            blocs_a_bouger.append((position_robot[0], position_robot[1] - i))
            i += 1
        if (position_robot[0], position_robot[1] - i) not in position_murs:
            for index in range(len(blocs_a_bouger) - 1, -1, -1):
                position_coffres.add((blocs_a_bouger[index][0], blocs_a_bouger[index][1] - 1))
                position_coffres.remove(blocs_a_bouger[index])
            position_robot[1] -= 1
            
def print_warehouse(): #used for debugging
    global position_murs, position_coffres, position_robot, warehouse
    to_print = ""
    for i in range(len(warehouse)):
        for j in range(len(warehouse[0])):
            if (i,j) in position_murs:
                to_print += "#"
            elif (i,j) in position_coffres:
                to_print += "O"
            elif [i,j] ==  position_robot:
                to_print += "@"
            else:
                to_print += "."
        to_print += "\n"
    print(to_print)
    
for i in range(len(instructions)):
    execute_instructions(instructions[i])

total = 0
for i in range(len(warehouse)):
    for j in range(len(warehouse[0])):
        if (i, j) in position_coffres:
            total += i * 100 + j
print(total)
#the answer was 1517819
