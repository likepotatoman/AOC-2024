"""
This code was written without my knowledge on the existence of caching.
I break apart the 75 blinks into 5 blocks of 15 and put the result of a certain number into the memory so that it would be calculated as well.
I basically tried reinvent caching from what I understood but in a way inefficient manner.
This was still a good learning experience :)
Sorry for the french variable names...
"""
entree_init = [1, 24596, 0, 740994, 60, 803, 8918, 9405859]
blink_result = {}

def blink(n):
    if n == 0:
        return [1]
    if len(str(n)) % 2 == 0:
        return [int(str(n)[:round(len(str(n)) / 2)]), int(str(n)[round(len(str(n)) / 2):])]
    else :
        return [n * 2024]

def blink_15_times(n):
    global blink_result
    if n in blink_result:
        return blink_result[n]
    else :
        entree = [n]
        for blink_times in range(15):
            nouvelle_entree = []
            for i in range(len(entree)):
                nouvelle_entree.append(blink(entree[i]))
            entree = []
            for i in range(len(nouvelle_entree)):
                for j in range(len(nouvelle_entree[i])):
                    entree.append(nouvelle_entree[i][j])
        blink_result[n] = entree
        return entree

total = 0
for i in range(len(entree_init)):
    depth1 = blink_15_times(entree_init[i])
    for j in range(len(depth1)):
        depth2 = blink_15_times(depth1[j])
        for k in range(len(depth2)):
            depth3 = blink_15_times(depth2[k])
            for h in range(len(depth3)):
                depth4 = blink_15_times(depth3[h])
                for g in range(len(depth4)):
                    depth5 = blink_15_times(depth4[g])
                    total += len(depth5)
            print("stone",str(i),str(j),str(k),"done") #to avoid time-outs

print(total)
