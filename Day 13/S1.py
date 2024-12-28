with open("C:/Users/dmlam/Desktop/AOC2024 D-13.txt", "r") as file:
    raw_data = file.read()
    lines = raw_data.splitlines()
print(len(lines)//4)

crane_games = []
for i in range(len(lines)//4 + 1):
    crane_games.append([])
    for j in range(3):
        indice_lettre = 0
        premier_nombre = ""
        deuxieme_nombre = ""
        while lines[i*4 + j][indice_lettre] != "X":
            indice_lettre += 1
        indice_lettre += 2
        while lines[i*4 + j][indice_lettre] != ",":
            premier_nombre += lines[i*4 + j][indice_lettre]
            indice_lettre += 1
        while lines[i*4 + j][indice_lettre] != "Y":
            indice_lettre += 1
        indice_lettre += 2
        while indice_lettre < len(lines[i*4+j]):
            deuxieme_nombre += lines[i*4 + j][indice_lettre]
            indice_lettre += 1
        crane_games[i].append([int(premier_nombre), int(deuxieme_nombre)])

def cheapest_solution(crane_game):
    possibilities = []
    total = [0,0]
    button_A_press = 0
    while crane_game[0][0] * button_A_press < crane_game[2][0] and crane_game[0][1] * button_A_press < crane_game[2][1]:
        button_B_press = 0
        while crane_game[0][0] * button_A_press + crane_game[1][0] * button_B_press < crane_game[2][0] and crane_game[0][1] * button_A_press + crane_game[1][1] * button_B_press < crane_game[2][1]:
            button_B_press += 1
        if crane_game[0][0] * button_A_press + crane_game[1][0] * button_B_press == crane_game[2][0] and crane_game[0][1] * button_A_press + crane_game[1][1] * button_B_press == crane_game[2][1]:
            possibilities.append([button_A_press, button_B_press])
        button_A_press += 1
    if possibilities != []:
        cheapest_solution = possibilities[0][0] * 3 + possibilities[0][1]
        for possibility in possibilities:
            if possibility[0] * 3 + possibility[1] < cheapest_solution:
                cheapest_solution = possibility[0] * 3 + possibility[1]
        return cheapest_solution
    else :
        return 0


total = 0
for crane_game in crane_games:
    total += cheapest_solution(crane_game)
print(total)
#the answer was 31623
