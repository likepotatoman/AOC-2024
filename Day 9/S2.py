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


def find_lowest_opening_index(n, data, slotted_number):
    length_opening = 0
    lowest_index = 0
    for i in range(len(data)):
        if data[i] == ".":
            if length_opening == 0:
                lowest_index = i
            length_opening += 1
        else :
            length_opening = 0
        if length_opening == n:
            return lowest_index
        if data[i] == slotted_number:
            return None
          
def stats_number(n,data):
    lowest_index_number = 0
    number_length = 0
    
    lowest_found = False
    for i in range(len(data)):
        if lowest_found == False:
            if data[i] == n:
                lowest_found = True
                lowest_index_number = i
                number_length += 1
        else :
            if data[i] == n:
                number_length += 1

    return number_length, lowest_index_number

counter = 0
for i in range(expended_data[-1], -1, -1):
    print("wait : processing memory displacement number "+ str(counter)) #this is just so that Thonny doesn't time out
    counter += 1 
    info_slotted = stats_number(i, expended_data)
    info_slot = find_lowest_opening_index(info_slotted[0], expended_data, i)
    if info_slot != None:
        for j in range(info_slotted[0]):
            expended_data[info_slot + j], expended_data[info_slotted[1] + j] = expended_data[info_slotted[1] + j], expended_data[info_slot + j]

total = 0
for i in range(len(expended_data)):
    if expended_data[i] != ".":
        total += expended_data[i]*i

print(total)
#the answer was 6307279963620
