with open("C:/Users/dmlam/Desktop/AOC2024 D-2.txt","r") as file:
    content = file.read()
    lines = content.splitlines()
data = []
for i in range(len(lines)):
    data.append(lines[i].split())

error = []
safe_amount = 0
for i in range(len(data)):
    safe = True
    if int(data[i][0]) >= int(data[i][1]):
        direction = False #decreasing
    else :
        direction = True #increasing
    for j in range(len(data[i])-1):
        if safe == True:
            if abs(int(data[i][j]) - int(data[i][j+1])) > 3:
                safe = False
            elif abs(int(data[i][j]) - int(data[i][j+1])) == 0:
                safe = False
            elif direction == True:
                if int(data[i][j]) > int(data[i][j+1]):
                    safe = False
            elif direction == False:
                if int(data[i][j]) < int(data[i][j+1]):
                    safe = False
    if safe == True:
        safe_amount += 1

print(safe_amount)
#the answer was 585
