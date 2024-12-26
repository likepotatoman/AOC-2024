entree = [1, 24596, 0, 740994, 60, 803, 8918, 9405859]

def blink(n):
    if n == 0:
        return [1]
    if len(str(n)) % 2 == 0:
        return [int(str(n)[:round(len(str(n)) / 2)]), int(str(n)[round(len(str(n)) / 2):])]
    else :
        return [n * 2024]

print(blink(0))
print(blink(20500600680548))
print(blink(3))

for blink_times in range(25):
    nouvelle_entree = []
    print("blinked")
    for i in range(len(entree)):
        nouvelle_entree.append(blink(entree[i]))
    entree = []
    for i in range(len(nouvelle_entree)):
        for j in range(len(nouvelle_entree[i])):
            entree.append(nouvelle_entree[i][j])
print(len(entree))
#the answer was 203457
