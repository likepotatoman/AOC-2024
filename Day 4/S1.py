with open("AdventOfCode D-4 input.txt", "r") as file:
    content = file.read()
lines = content.splitlines()
matrice = []
for i in range(len(lines)):
    matrice.append(list(lines[i]))
final_total = 0

def check_line(line):
    total = 0
    stages = ["X","M","A","S"]
    current_stage = -1
    for i in range(len(line)):
        char = line[i]
        if char == "X":
            current_stage = 0
        else :
            if char == stages[current_stage + 1]:
                current_stage += 1
            else :
                current_stage = -1
            if current_stage == 3:
                total += 1
                current_stage = -1
    return total

def rotate(matrice):
    rotated_matrice = []
    for i in range(len(matrice[0])):
        rotated_matrice.append([])
        for j in range(len(matrice)):
            rotated_matrice[i].append(matrice[len(matrice) - j - 1][i])
    return rotated_matrice

def flip(matrice):
    flipped_matrice = []
    for i in range(len(matrice)):
        line = list(matrice[i])
        line.reverse()
        flipped_matrice.append(line)
    return flipped_matrice

def diagonal_read(matrice):
    diagonal_read_matrice = []
    for i in range(len(matrice)):
        line = []
        j = i
        k = 0
        while j >= 0:
            line.append(matrice[j][k])
            k += 1
            j -= 1
        diagonal_read_matrice.append(line)
    
    for i in range(1,len(matrice[0])):
        line = []
        j = len(matrice) - 1
        k = i
        while k < len(matrice[0]):
            line.append(matrice[j][k])
            k += 1
            j -= 1
        diagonal_read_matrice.append(line)
    return diagonal_read_matrice
    

#de la gauche
test_matrice = matrice
for i in range(len(matrice)):
    total_final += check_line(test_matrice[i])

#de la droite
test_matrice = flip(matrice)
for i in range(len(matrice)):
    total_final += check_line(test_matrice[i])

#du haut
test_matrice = flip(rotate(matrice))
for i in range(len(matrice[i])):
    total_final += check_line(test_matrice[i])

#du bas
test_matrice = rotate(matrice)
for i in range(len(matrice)):
    total_final += check_line(test_matrice[i])

#du diagonal haut gauche
test_matrice = diagonal_read(matrice)
for i in range(len(matrice)):
    total_final += check_line(test_matrice[i])

#du diagonal haut droit
test_matrice = diagonal_read(flip(matrice))
for i in range(len(matrice)):
    total_final += check_line(test_matrice[i])

#du diagonal bas gauche
test_matrice = flip(diagonal_read((flip(matrice)))
for i in range(len(matrice)):
    total_final += check_line(test_matrice[i])

#du diagonal bas droit
test_matrice = flip(diagonal_read(matrice))
for i in range(len(matrice)):
    total_final += check_line(test_matrice[i])

print(total_final)
