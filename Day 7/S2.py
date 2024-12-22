with open("C:/Users/dmlam/Desktop/AOC2024 D-7.txt", "r") as file:
    content = file.read()
    lines = content.splitlines()  # This returns a list of lines, with newline characters
    
holder = []
for i in range(len(lines)):
    holder.append(lines[i].split())
    
equations = []
for i in range(len(holder)):
    equations.append([])
    final_number = int(holder[i][0][0:len(holder[i][0])-1])
    equations[i].append(final_number)
    list_of_numbers = []
    for j in range(1,len(holder[i])):
        list_of_numbers.append(int(holder[i][j]))
    equations[i].append(list_of_numbers)

def convert_base3(n):
    liste_reponse = ""
    plus_grande_puissance = 0
    while 3**(plus_grande_puissance + 1) <= n:
        plus_grande_puissance += 1

    for i in range(plus_grande_puissance,-1,-1):
        c = 0
        while 3**i <= n:
            c += 1
            n = n - 3**i
        liste_reponse += str(c)
    return liste_reponse

def possible_permutations(n):
    permutations = []
    
    for i in range(3**(n-1)):
        permutation_string = ""
        for j in range(n - 1 - len(convert_base3(i))):
            permutation_string += "0"
        permutation_string += convert_base3(i)
        permutation_list = []
        for i in range(len(permutation_string)):
            permutation_list.append(int(permutation_string[i]))
        permutations.append(permutation_list)
    return permutations

def permutation_correcte(but, liste_de_nombre, permutation):
    total = liste_de_nombre[0]
    
    for i in range(1, len(liste_de_nombre)):
        if permutation[i-1] == 0:
            total += liste_de_nombre[i]
        elif permutation[i-1] == 1:
            total *= liste_de_nombre[i]
        else :
            total = str(total)
            total += str(liste_de_nombre[i])
            total = int(total)
    if but == total:
        return True
    return False

total = 0
for i in range(len(equations)):
    possible = False
    for permutation in possible_permutations(len(equations[i][1])):
        if possible == False:
            if permutation_correcte(equations[i][0], equations[i][1], permutation) == True:
                possible = True
                print(permutation)
                print(equations[i])
                print("\n")
    if possible == True:
        total += equations[i][0]
        print(total)
print(total)
#the answer was 105517128211543
