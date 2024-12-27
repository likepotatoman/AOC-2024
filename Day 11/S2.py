entree_init = [1, 24596, 0, 740994, 60, 803, 8918, 9405859]

from functools import cache

@cache
def blink(n, steps):
    if steps == 0:
        return 1
    if n == 0:
        return blink(1, steps - 1)
    elif len(str(n)) % 2 == 0:
        return blink(int(str(n)[:round(len(str(n)) / 2)]),steps - 1) + blink(int(str(n)[round(len(str(n)) / 2):]),steps - 1)
    else :
        return blink(n * 2024, steps - 1)

total = 0
for i in range(len(entree_init)):
        total += blink(entree_init[i], 75)
print(total)
#the answer was 241394363462435
