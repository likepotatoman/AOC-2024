with open("C:/Users/dmlam/Desktop/AOC2024 D-9.txt", "r") as file:
    raw_data = list(file.read())

expended_data = []
for i in range(len(raw_data)):
    if i % 2 == 0:
        for j in range(int(raw_data[i])):
            expended_data.append(i//2)
    if i % 2 == 1:
        for j in range(int(raw_data[i])):
            expended_data.append(".")


def filled(data):
    hole = False
    for i in range(len(data)):
        if data[i] == ".":
            hole = True
        if hole == True:
            if data[i] != ".":
                return False
    return True

index_lowest_space = 0
index_highest_filled = len(expended_data) - 1
counter = 0
while filled(expended_data) != True:
    print("wait : processing memory displacement number "+ str(counter)) #this is just so that Thonny doesn't time out
    counter += 1
    while expended_data[index_lowest_space] != ".":
        index_lowest_space += 1
    while expended_data[index_highest_filled] == ".":
        index_highest_filled -= 1
    expended_data[index_lowest_space], expended_data[index_highest_filled] = expended_data[index_highest_filled], expended_data[index_lowest_space]

i = 0
total = 0
while expended_data[i] != ".":
    total += expended_data[i]*i
    i += 1
print(total)

