with open("C:/Users/dmlam/Desktop/AOC2024 D-14.txt", "r") as file:
    raw_data = file.read()
    lines = raw_data.splitlines()

import time

robots = []
for i in range(len(lines)):
    robots.append([])
    indice_lettre = 0
    premier_nombre = ""
    deuxieme_nombre = ""
    while lines[i][indice_lettre] != "=":
        indice_lettre += 1
    indice_lettre += 1
    while lines[i][indice_lettre] != ",":
        premier_nombre += lines[i][indice_lettre]
        indice_lettre += 1
    indice_lettre += 1
    while lines[i][indice_lettre] != " ":
        deuxieme_nombre += lines[i][indice_lettre]
        indice_lettre += 1
    robots[i].append([int(premier_nombre), int(deuxieme_nombre)])
    premier_nombre = ""
    deuxieme_nombre = ""
    while lines[i][indice_lettre] != "=":
        indice_lettre += 1
    indice_lettre += 1
    while lines[i][indice_lettre] != ",":
        premier_nombre += lines[i][indice_lettre]
        indice_lettre += 1
    indice_lettre += 1
    while indice_lettre < len(lines[i]):
        deuxieme_nombre += lines[i][indice_lettre]
        indice_lettre += 1
    robots[i].append([int(premier_nombre), int(deuxieme_nombre)])

def wait_1_second(robot_data):
    for i in range(len(robot_data)):
        robot_data[i][0][0] += robot_data[i][1][0]
        robot_data[i][0][1] += robot_data[i][1][1]
        while robot_data[i][0][0] < 0:
            robot_data[i][0][0] += 101
        while robot_data[i][0][0] > 100:
            robot_data[i][0][0] -= 101
            
        while robot_data[i][0][1] < 0:
            robot_data[i][0][1] += 103
        while robot_data[i][0][1] > 102:
            robot_data[i][0][1] -= 103
    return robot_data

def display_map(robots):
    positions = [point[0] for point in robots]
    for i in range(103):
        line = ""
        for j in range(101):
            if [j, i] in positions:
                line += "+"
            else :
                line += " "
        print(line)

i = 0
while True:
    print(str(i))
    display_map(robots) #we just check until it's good
    robots = wait_1_second(robots)
    i += 1
    time.sleep(1)
#the answer was 7383
