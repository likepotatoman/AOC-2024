#import time #for visualisation only

with open("C:/Users/dmlam/Desktop/AOC2024 D-15 instructions.txt", "r") as file:
    instructions = file.read()

with open("C:/Users/dmlam/Desktop/AOC2024 D-15 map.txt", "r") as file:
    raw_data = file.read()
    lines = raw_data.splitlines()

warehouse = []
for i in range(len(lines)):
    warehouse.append(list(lines[i]))
position_murs = set()
position_coffres_gauche = set()
position_coffres_droite = set()


for i in range(len(warehouse)):
    for j in range(len(warehouse[0])):
        if warehouse[i][j] == "#":
            position_murs.add((i, j*2))
            position_murs.add((i, j*2 + 1))
        elif warehouse[i][j] == "O":
            position_coffres_gauche.add((i, j*2))
            position_coffres_droite.add((i, j*2 + 1))
        elif warehouse[i][j] == "@":
            position_robot = [i,j*2]


def execute_instructions(instruction):
    global position_murs, position_coffres_gauche, position_coffres_droite, position_robot
    blocs_a_bouger = []
    
    if instruction == "^":
        wall_detected = False
        highest_row = [position_robot]
        if (position_robot[0] - 1, position_robot[1]) in position_coffres_gauche or (position_robot[0] -1, position_robot[1]) in position_coffres_droite:
            all_open = False
        else :
            all_open = True
        if (position_robot[0] - 1, position_robot[1]) in position_murs:
            wall_detected = True
            
        while wall_detected == False and all_open == False:
            nouveau_blocs = 0 
            all_open = True
            for j in range(len(highest_row)):
                if (highest_row[j][0] - 1, highest_row[j][1]) in position_coffres_gauche:
                    if (highest_row[j][0] - 1, highest_row[j][1], "[") not in blocs_a_bouger:
                        all_open = False
                        blocs_a_bouger.append((highest_row[j][0] - 1, highest_row[j][1], "["))
                        blocs_a_bouger.append((highest_row[j][0] - 1, highest_row[j][1] + 1, "]"))
                        nouveau_blocs += 2
                elif (highest_row[j][0] - 1, highest_row[j][1]) in position_coffres_droite:
                    if (highest_row[j][0] - 1, highest_row[j][1], "]") not in blocs_a_bouger:
                        all_open = False
                        blocs_a_bouger.append((highest_row[j][0] - 1, highest_row[j][1], "]"))
                        blocs_a_bouger.append((highest_row[j][0] - 1, highest_row[j][1] - 1, "["))
                        nouveau_blocs += 2
                elif (highest_row[j][0] - 1, highest_row[j][1]) in position_murs:
                    wall_detected = True
                    
            highest_row = blocs_a_bouger[-nouveau_blocs:]
        
        if wall_detected == False:
            for index in range(len(blocs_a_bouger) - 1, -1, -1):
                if blocs_a_bouger[index][2] == "[":
                    position_coffres_gauche.add((blocs_a_bouger[index][0] - 1, blocs_a_bouger[index][1]))
                    position_coffres_gauche.remove((blocs_a_bouger[index][0], blocs_a_bouger[index][1]))
                if blocs_a_bouger[index][2] == "]":
                    position_coffres_droite.add((blocs_a_bouger[index][0] - 1, blocs_a_bouger[index][1]))
                    position_coffres_droite.remove((blocs_a_bouger[index][0], blocs_a_bouger[index][1]))
            position_robot[0] -= 1            
        
    if instruction == "v":
        wall_detected = False
        highest_row = [position_robot]
        if (position_robot[0] + 1, position_robot[1]) in position_coffres_gauche or (position_robot[0] + 1, position_robot[1]) in position_coffres_droite:
            all_open = False
        else :
            all_open = True
        if (position_robot[0] + 1, position_robot[1]) in position_murs:
            wall_detected = True
            
        while wall_detected == False and all_open == False:
            nouveau_blocs = 0 
            all_open = True
            for j in range(len(highest_row)):
                if (highest_row[j][0] + 1, highest_row[j][1]) in position_coffres_gauche:
                    if (highest_row[j][0] + 1, highest_row[j][1], "[") not in blocs_a_bouger:
                        all_open = False
                        blocs_a_bouger.append((highest_row[j][0] + 1, highest_row[j][1], "["))
                        blocs_a_bouger.append((highest_row[j][0] + 1, highest_row[j][1] + 1, "]"))
                        nouveau_blocs += 2
                elif (highest_row[j][0] + 1, highest_row[j][1]) in position_coffres_droite:
                    if (highest_row[j][0] + 1, highest_row[j][1], "]") not in blocs_a_bouger:
                        all_open = False
                        blocs_a_bouger.append((highest_row[j][0] + 1, highest_row[j][1], "]"))
                        blocs_a_bouger.append((highest_row[j][0] + 1, highest_row[j][1] - 1, "["))
                        nouveau_blocs += 2
                elif (highest_row[j][0] + 1, highest_row[j][1]) in position_murs:
                    wall_detected = True
            highest_row = blocs_a_bouger[-nouveau_blocs:]
        
        if wall_detected == False:
            for index in range(len(blocs_a_bouger) - 1, -1, -1):
                if blocs_a_bouger[index][2] == "[":
                    position_coffres_gauche.add((blocs_a_bouger[index][0] + 1, blocs_a_bouger[index][1]))
                    position_coffres_gauche.remove((blocs_a_bouger[index][0], blocs_a_bouger[index][1]))
                if blocs_a_bouger[index][2] == "]":
                    position_coffres_droite.add((blocs_a_bouger[index][0] + 1, blocs_a_bouger[index][1]))
                    position_coffres_droite.remove((blocs_a_bouger[index][0], blocs_a_bouger[index][1]))
            position_robot[0] += 1  


    if instruction == ">":
        i = 1
        while (position_robot[0], position_robot[1] + i) not in  position_murs and ( (position_robot[0], position_robot[1] + i) in position_coffres_gauche or (position_robot[0], position_robot[1] + i) in position_coffres_droite ):
            if (position_robot[0], position_robot[1] + i) in position_coffres_gauche:
                blocs_a_bouger.append((position_robot[0], position_robot[1] + i, "["))
            if (position_robot[0], position_robot[1] + i) in position_coffres_droite:
                blocs_a_bouger.append((position_robot[0], position_robot[1] + i, "]"))
            i += 1
        if (position_robot[0], position_robot[1] + i) not in position_murs:
            for index in range(len(blocs_a_bouger) - 1, -1, -1):
                if blocs_a_bouger[index][2] == "[":
                    position_coffres_gauche.add((blocs_a_bouger[index][0], blocs_a_bouger[index][1] + 1))
                    position_coffres_gauche.remove((blocs_a_bouger[index][0], blocs_a_bouger[index][1]))
                if blocs_a_bouger[index][2] == "]":
                    position_coffres_droite.add((blocs_a_bouger[index][0], blocs_a_bouger[index][1] + 1))
                    position_coffres_droite.remove((blocs_a_bouger[index][0], blocs_a_bouger[index][1]))
            position_robot[1] += 1

    if instruction == "<":
        i = 1
        while (position_robot[0], position_robot[1] - i) not in  position_murs and ( (position_robot[0], position_robot[1] - i) in position_coffres_gauche or (position_robot[0], position_robot[1] - i) in position_coffres_droite):
            if (position_robot[0], position_robot[1] - i) in position_coffres_gauche:
                blocs_a_bouger.append((position_robot[0], position_robot[1] - i, "["))
            if (position_robot[0], position_robot[1] - i) in position_coffres_droite:
                blocs_a_bouger.append((position_robot[0], position_robot[1] - i, "]"))
            i += 1
        if (position_robot[0], position_robot[1] - i) not in position_murs:
            for index in range(len(blocs_a_bouger) - 1, -1, -1):
                if blocs_a_bouger[index][2] == "[":
                    position_coffres_gauche.add((blocs_a_bouger[index][0], blocs_a_bouger[index][1] - 1))
                    position_coffres_gauche.remove((blocs_a_bouger[index][0], blocs_a_bouger[index][1]))
                if blocs_a_bouger[index][2] == "]":
                    position_coffres_droite.add((blocs_a_bouger[index][0], blocs_a_bouger[index][1] - 1))
                    position_coffres_droite.remove((blocs_a_bouger[index][0], blocs_a_bouger[index][1]))
            position_robot[1] -= 1
            
def print_warehouse(): #used for debugging 
    global position_murs, position_coffres_gauche, position_coffres_droite, position_robot, warehouse
    to_print = ""
    for i in range(len(warehouse)):
        for j in range(len(warehouse[0]) * 2):
            if (i,j) in position_murs:
                to_print += "#"
            elif (i,j) in position_coffres_gauche:
                to_print += "["
            elif (i,j) in position_coffres_droite:
                to_print += "]"
            elif [i,j] ==  position_robot:
                to_print += "@"
            else:
                to_print += "."
        to_print += "\n"
    print(to_print)

print_warehouse()
for i in range(len(instructions)):
    execute_instructions(instructions[i])
    #time.sleep(0.2) #use for visualization
    #print_warehouse()
    #print(instructions[i])

total = 0
for i in range(len(warehouse)):
    for j in range(len(warehouse[0])*2):
        if (i, j) in position_coffres_gauche:
            total += i * 100 + j
print(total)
#the answer is 1538862
