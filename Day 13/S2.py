"""
Disclaimer that I had a lot of trouble figuring out the system of equation for some reason so I had to watch a video.
In my defense, they made it sound as if there would be multiple possible solutions so that made me discard equation systems from the get go (which I obviously shouldn't have).
In my defense 2, its 2 in the morning so I;m not particularly mathematically sharp right now...
"""

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
for i in range(len(crane_games)):
    crane_games[i][2][0], crane_games[i][2][1] = crane_games[i][2][0] + 10000000000000, crane_games[i][2][1] + 10000000000000


def cheapest_solution(crane_game):
    t = (crane_game[2][1] * crane_game[0][0] - crane_game[0][1] * crane_game[2][0]) / (crane_game[1][1] * crane_game[0][0] - crane_game[0][1] * crane_game[1][0])
    s = (crane_game[2][0] - crane_game[1][0] * t) / crane_game[0][0]
    print(t)
    if t % 1 == 0:
        return s * 3 + t
    else :
        return 0


total = 0
for crane_game in crane_games:
    total += cheapest_solution(crane_game)
print(int(total))
#the answer was 93209116744825
