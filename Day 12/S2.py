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

def count_sides(positions):
    #direction == 0 --> Droite
    #direction == 0 --> Haut
    #direction == 0 --> Gauche
    #direction == 0 --> Bas
    #En gros c'est dans le sens du cercle trigonometrique
    
    number_of_sides = 0
    position_liste = list(positions)
    for direction in range(4):
        position_of_interest = find_position_of_interest(position_liste, direction)
        number_of_sides += find_sides(position_of_interest, direction)
    
    return number_of_sides * len(positions)
    
def find_sides(position_of_interest, direction):
    total = 0
    if direction % 2 == 0:
        point_haut = min([position[0] for position in position_of_interest])
        point_bas = max([position[0] for position in position_of_interest])
        
        for hauteur in range(point_haut, point_bas + 1):
            points_concernes = [point for point in position_of_interest if point[0] == hauteur]
            for i in range(len(points_concernes)):
                if (points_concernes[i][0] + 1, points_concernes[i][1]) not in position_of_interest:
                    total += 1
    
    else :
        point_droite = max([position[1] for position in position_of_interest])
        point_gauche = min([position[1] for position in position_of_interest])
        
        for hauteur in range(point_gauche, point_droite + 1):
            points_concernes = [point for point in position_of_interest if point[1] == hauteur]
            for i in range(len(points_concernes)):
                if (points_concernes[i][0], points_concernes[i][1] + 1) not in position_of_interest:
                    total += 1
        
    return total 
        
    

def find_position_of_interest(positions, direction):
    position_of_interest = []
    if direction == 0:
        for i in range(len(positions)):
            if (positions[i][0], positions[i][1] + 1) not in positions:
                position_of_interest.append(positions[i])
    elif direction == 2:
        for i in range(len(positions)):
            if (positions[i][0], positions[i][1] - 1) not in positions:
                position_of_interest.append(positions[i])
    elif direction == 1:
        for i in range(len(positions)):
            if (positions[i][0] - 1, positions[i][1]) not in positions:
                position_of_interest.append(positions[i])
    else :
        for i in range(len(positions)):
            if (positions[i][0] + 1, positions[i][1]) not in positions:
                position_of_interest.append(positions[i])
    return position_of_interest



total = 0
while coordinates_to_check != []:
        total += count_sides(flood({coordinates_to_check[0]},garden[coordinates_to_check[0][0]][coordinates_to_check[0][1]], garden))
        coordinates_to_remove = list(flood({coordinates_to_check[0]},garden[coordinates_to_check[0][0]][coordinates_to_check[0][1]], garden))
        for i in range(len(coordinates_to_remove)):
            coordinates_to_check.remove(coordinates_to_remove[i])
print(total)
#the answer was 909564
