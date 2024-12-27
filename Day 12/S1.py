with open("C:/Users/dmlam/Desktop/AOC2024 D-12.txt", "r") as file:
    raw_data = file.read()
    maps = raw_data.splitlines()

garden = []
for i in range(len(maps)):
    garden.append(list(maps[i]))

coordinates_to_check = []
for i in range(len(garden)):
    for j in range(len(garden[0])):
        coordinates_to_check.append((i,j))

def flood(positions, lettre, garden):
    initial_positions = set(positions)
    position_liste = list(positions)
    for i in range(len(position_liste)):
        if position_liste[i][0] != 0:
            if garden[position_liste[i][0] - 1][position_liste[i][1]] == lettre:
                positions.add(tuple([position_liste[i][0] - 1, position_liste[i][1]]))  
        if position_liste[i][0] != len(garden) - 1:
            if garden[position_liste[i][0] + 1][position_liste[i][1]] == lettre:
                positions.add(tuple([position_liste[i][0] + 1, position_liste[i][1]]))   
        if position_liste[i][1] != 0:
            if garden[position_liste[i][0]][position_liste[i][1] - 1] == lettre:
                positions.add(tuple([position_liste[i][0], position_liste[i][1] - 1]))      
        if position_liste[i][1] != len(garden[0]) - 1:
            if garden[position_liste[i][0]][position_liste[i][1] + 1] == lettre:
                positions.add(tuple([position_liste[i][0], position_liste[i][1] + 1]))
    if positions == initial_positions:
        return positions
    return flood(positions, lettre, garden)

def calculate(positions):
    position_liste = list(positions)
    fence = 0
    for i in range(len(position_liste)):
        if (position_liste[i][0] - 1, position_liste[i][1]) not in positions:
            fence += 1
        if (position_liste[i][0] + 1, position_liste[i][1]) not in positions:
            fence += 1 
        if (position_liste[i][0], position_liste[i][1] - 1) not in positions:
            fence += 1
        if (position_liste[i][0], position_liste[i][1] + 1) not in positions:
            fence += 1
    return fence * len(positions)

total = 0
while coordinates_to_check != []:
        total += calculate(flood({coordinates_to_check[0]},garden[coordinates_to_check[0][0]][coordinates_to_check[0][1]], garden))
        coordinates_to_remove = list(flood({coordinates_to_check[0]},garden[coordinates_to_check[0][0]][coordinates_to_check[0][1]], garden))
        for i in range(len(coordinates_to_remove)):
            coordinates_to_check.remove(coordinates_to_remove[i])
print(total)
#the answer was 1518548
