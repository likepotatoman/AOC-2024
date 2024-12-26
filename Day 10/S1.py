with open("C:/Users/dmlam/Desktop/AOC2024 D-10.txt", "r") as file:
    raw_data = file.read()
    maps = raw_data.splitlines()

topographic_str = []
for i in range(len(maps)):
    topographic_str.append(list(maps[i]))

topographic = []
for i in range(len(topographic_str)):
    topographic.append([])
    for j in range(len(topographic_str[0])):
        topographic[i].append(int(topographic_str[i][j]))

def nombre_chemins(position_initiale, data):
    liste_chemins = [[position_initiale]]
    for i in range(1, 10):
        for j in range(len(liste_chemins)):
            derniere_position = liste_chemins[0][-1]
            if derniere_position[0] != 0:
                if data[derniere_position[0] - 1][derniere_position[1]] == i:
                    nouvelle_liste = list(liste_chemins[0])
                    nouvelle_liste.append(list([derniere_position[0] - 1, derniere_position[1]]))
                    liste_chemins.append(list(nouvelle_liste))
            if derniere_position[0] != len(data) - 1:
                if data[derniere_position[0] + 1][derniere_position[1]] == i:
                    nouvelle_liste = list(liste_chemins[0])
                    nouvelle_liste.append(list([derniere_position[0] + 1, derniere_position[1]]))
                    liste_chemins.append(list(nouvelle_liste))
            if derniere_position[1] != 0:
                if data[derniere_position[0]][derniere_position[1] - 1] == i:
                    nouvelle_liste = list(liste_chemins[0])
                    nouvelle_liste.append(list([derniere_position[0], derniere_position[1] - 1]))
                    liste_chemins.append(list(nouvelle_liste))
            if derniere_position[1] != len(data[0]) - 1:
                if data[derniere_position[0]][derniere_position[1] + 1] == i:
                    nouvelle_liste = list(liste_chemins[0])
                    nouvelle_liste.append(list([derniere_position[0], derniere_position[1] + 1]))
                    liste_chemins.append(list(nouvelle_liste))
            liste_chemins.pop(0)
    pics_finaux = []
    for i in range(len(liste_chemins)):
        if liste_chemins[i][-1] not in pics_finaux:
            pics_finaux.append(liste_chemins[i][-1])
    
    return len(pics_finaux)
        
total = 0
for i in range(len(topographic)):
    for j in range(len(topographic[0])):
        if topographic[i][j] == 0:
            total += nombre_chemins([i,j],topographic)
print(total)
#the answer was 611
