with open("C:/Users/dmlam/Desktop/AOC2024 D-14.txt", "r") as file:
    raw_data = file.read()
    lines = raw_data.splitlines()

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

for i in range(100):
    robots = wait_1_second(robots)

quadrant1 = len([position_robot for position_robot in robots if 0 <= position_robot[0][0] <= 49 and 0 <= position_robot[0][1] <= 50])
quadrant2 = len([position_robot for position_robot in robots if 51 <= position_robot[0][0] <= 100 and 0 <= position_robot[0][1] <= 50])
quadrant3 = len([position_robot for position_robot in robots if 0 <= position_robot[0][0] <= 49 and 52 <= position_robot[0][1] <= 102])
quadrant4 = len([position_robot for position_robot in robots if 51 <= position_robot[0][0] <= 100 and 52 <= position_robot[0][1] <= 102])
print(quadrant1 * quadrant2 * quadrant3 * quadrant4)
#the answer was 229069152
