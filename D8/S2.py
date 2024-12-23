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

def find_antinode(position_antenna_1,position_antenna_2):
    antinodes = []
    delta_vector = [position_antenna_2[0] - position_antenna_1[0], position_antenna_2[1] - position_antenna_1[1]]
    i = -1
    antinode_potentielle = [position_antenna_2[0] + i*delta_vector[0], position_antenna_2[1] + i*delta_vector[1]]    
    while 0 <= antinode_potentielle[0] < 50 and 0 <= antinode_potentielle[1] < 50:
        antinodes.append(antinode_potentielle)
        i -= 1
        antinode_potentielle = [position_antenna_2[0] + i*delta_vector[0], position_antenna_2[1] + i*delta_vector[1]]
    i = 1
    antinode_potentielle = [position_antenna_1[0] + i*delta_vector[0], position_antenna_1[1] + i*delta_vector[1]]    
    while 0 <= antinode_potentielle[0] < 50 and 0 <= antinode_potentielle[1] < 50:
        antinodes.append(antinode_potentielle)
        i += 1
        antinode_potentielle = [position_antenna_1[0] + i*delta_vector[0], position_antenna_1[1] + i*delta_vector[1]]
    return antinodes

position_antinode = []
for i in range(len(position_antennas)):
    for j in range(len(position_antennas[i][1])-1):
        for k in range(j+1, len(position_antennas[i][1])):
            antinodes = find_antinode(position_antennas[i][1][j], position_antennas[i][1][k])
            for h in range(len(antinodes)):
                if antinodes[h] not in position_antinode:
                    position_antinode.append(antinodes[h])
                
print(len(position_antinode))
#the answer was 1333
