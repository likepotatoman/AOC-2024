with open("C:/Users/dmlam/Desktop/AOC2024 D-8.txt", "r") as file:
    content = file.read()
    lines = content.splitlines()  # This returns a list of lines, with newline characters
    
antenna_map = []
for i in range(len(lines)):
    antenna_map.append(list(lines[i]))

flattened = [item for sublist in antenna_map for item in sublist]
antennas = list(set(flattened))
antennas.remove(".")

position_antennas = []
for i in range(len(antennas)):
    position_antennas.append([])
    position_antennas[i].append(antennas[i])
    positions = []
    for j in range(len(antenna_map)):
        for k in range(len(antenna_map[0])):
            if  antenna_map[j][k] == antennas[i]:
                positions.append([j,k])
    position_antennas[i].append(positions)

position_antinode = []
for i in range(len(position_antennas)):
    for j in range(len(position_antennas[i][1])-1):
        for k in range(j+1, len(position_antennas[i][1])):
            delta_vector = [position_antennas[i][1][k][0] - position_antennas[i][1][j][0], position_antennas[i][1][k][1] - position_antennas[i][1][j][1]]
            antinode_potentielle_1 = [position_antennas[i][1][j][0] - delta_vector[0], position_antennas[i][1][j][1] - delta_vector[1]]
            antinode_potentielle_2 = [position_antennas[i][1][k][0] + delta_vector[0], position_antennas[i][1][k][1] + delta_vector[1]]
            if antinode_potentielle_1 not in position_antinode and  0 <= antinode_potentielle_1[0] < 50 and 0 <= antinode_potentielle_1[1] < 50:
                position_antinode.append(antinode_potentielle_1)
            if antinode_potentielle_2 not in position_antinode and  0 <= antinode_potentielle_2[0] < 50 and 0 <= antinode_potentielle_2[1] < 50:
                position_antinode.append(antinode_potentielle_2)
print(len(position_antinode))
#the answer was 398
