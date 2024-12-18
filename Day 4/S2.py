with open("C:/Users/dmlam/Desktop/AOC2024 D-4.txt","r") as file:
    content = file.read()
    lines = content.splitlines()
prep_matrice = []
for i in range(len(lines)):
    prep_matrice.append(list(lines[i]))
total_final = 0

matrice = []
for i in range(len(prep_matrice)):
    matrice.append([])
    for j in range(len(prep_matrice[0])):
        matrice[i].append([prep_matrice[i][j],i,j])


def check_line(line):
    position = []
    stages = ["M","A","S"]
    current_stage = -1
    for i in range(len(line)):
        char = line[i][0]
        if char == "X":
            current_stage = -1
        elif char == "M":
            current_stage = 0
        else :
            if char == stages[current_stage + 1]:
                current_stage += 1
            else :
                current_stage = -1
            if current_stage == 2:
                position.append([line[i-1][1],line[i-1][2]])
                current_stage = -1
    return position

def rotate(matrice):
    rotated_matrice = []
    for i in range(len(matrice[0])):
        rotated_matrice.append([])
        for j in range(len(matrice)):
            rotated_matrice[i].append(matrice[len(matrice) - j - 1][i])
    return rotated_matrice


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


#du diagonal haut gauche
test_matrice = diagonal_read(matrice)
diag= []
for i in range(len(test_matrice)):
    diag.append(check_line(test_matrice[i]))

#du diagonal haut droit
test_matrice = diagonal_read(rotate(matrice))
for i in range(len(test_matrice)):
    diag.append(check_line(test_matrice[i]))

#du diagonal bas gauche
test_matrice = diagonal_read(rotate(rotate(matrice)))
for i in range(len(test_matrice)):
    diag.append(check_line(test_matrice[i]))

#du diagonal bas droit
test_matrice = diagonal_read(rotate(rotate(rotate(matrice))))
for i in range(len(test_matrice)):
    diag.append(check_line(test_matrice[i]))

final_diag = []
for i in range(len(diag)):
    for j in range(len(diag[i])):
        final_diag.append(diag[i][j])

for i in range(len(final_diag)):
    for j in range(i+1, len(final_diag)):
        if final_diag[i] == final_diag[j]:
            total_final += 1

print(total_final)
#the answer was 1815
