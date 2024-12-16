with open("AdventOfCode D-1 input.txt", "r") as file:
    content = file.read()
    lines = content.splitlines()

liste_1 = []
liste_2 = []
for i in range(len(lines)):
    mots = lines[i].split()
    liste_1.append(int(mots[0]))
    liste_2.append(int(mots[1]))

liste_paires = []
index = 0
while liste_1 != []:
    liste_paires.append([])
    minimum1 = min(liste_1)
    liste_paires[index].append(minimum1)
    minimum2 = min(liste_2)
    liste_paires[index].append(minimum2)
    liste_1.remove(minimum1)
    liste_2.remove(minimum2)
    index += 1

total = 0
for i in range(len(liste_paires)):
    nombre = liste_paires[i][0]
    occurences = 0
    for j in range(len(liste_paires)):
        if liste_paires[j][1] == nombre:
            occurences += 1
    total += nombre*occurences
print(total)

#the answer was 26593248
