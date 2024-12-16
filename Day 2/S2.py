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
                error.append(data[i])
            elif abs(int(data[i][j]) - int(data[i][j+1])) == 0:
                safe = False
                error.append(data[i])
            elif direction == True:
                if int(data[i][j]) > int(data[i][j+1]):
                    safe = False
                    error.append(data[i])
            elif direction == False:
                if int(data[i][j]) < int(data[i][j+1]):
                    safe = False
                    error.append(data[i])
    if safe == True:
        safe_amount += 1

def check(liste):
    safe = True
    if int(liste[0]) >= int(liste[1]):
        direction = False #decreasing
    else :
        direction = True #increasing
    for j in range(len(liste)-1):
        if abs(int(liste[j]) - int(liste[j+1])) > 3:
            safe = False
        if abs(int(liste[j]) - int(liste[j+1])) == 0:
            safe = False
        if direction == True:
            if int(liste[j]) > int(liste[j+1]):
                safe = False
        if direction == False:
            if int(liste[j]) < int(liste[j+1]):
                safe = False
    return safe
  
for i in range(len(error)):
    safe = False
    for j in range(len(error[i])):
        if safe == False:
            to_check = list(error[i])
            to_check.pop(j)
            if check(to_check) == True:
                safe = True
                safe_amount += 1
       
print(safe_amount)
#the answer was 626
