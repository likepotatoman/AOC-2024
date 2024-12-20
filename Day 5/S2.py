with open("AOC2024 D-5 Input1.txt", "r") as file:
    content = file.read()
    lines = content.splitlines()
rules = []
for i in range(len(lines)):
    j = 0
    first_number = ""
    second_number = ""
    while lines[i][j] != "|":
        first_number += lines[i][j]
        j += 1
    j += 1
    for k in range(j,len(lines[i])):
        second_number += lines[i][k]
    rules.append([int(first_number), int(second_number)])


with open("AOC2024 D-5 Input2.txt", "r") as file:
    content = file.read()
    lines = content.splitlines()
    updates_prep = []
for i in range(len(lines)):
    updates_prep.append(list(lines[i]))

updates = []
for i in range(len(updates_prep)):
    updates.append([])
    number= ""
    for j in range(len(updates_prep[i])):
        if updates_prep[i][j] == ",":
            updates[i].append(int(number))
            number = ""
        else : 
            number += updates_prep[i][j]
    updates[i].append(int(number))

def check(update, rule):
    if rule[0] in update and rule[1] in update:
        for i in range(len(update)):
            if update[i] == rule[0]:
                return True
            if update[i] == rule[1]:
                return False
        
    else : 
        return True

def order(numbers, rules):
        all_numbers = list(numbers)
        ordered = [numbers[0]]
        all_numbers.pop(0)
        checked_number_index = 0

        while len(ordered) != len(numbers):
            checked_number = all_numbers[checked_number_index]
            maximum_index = len(ordered)
            minimum_index = 0
            for i in range(len(rules)):
                if rules[i][0] == checked_number:
                    if rules[i][1] in ordered:
                        if ordered.index(rules[i][1]) < maximum_index : 
                            maximum_index = ordered.index(rules[i][1])
                
                if rules[i][1] == checked_number:
                    if rules[i][0] in ordered:
                        if ordered.index(rules[i][0]) + 1 > minimum_index : 
                            minimum_index = ordered.index(rules[i][0]) + 1
            checked_number_index += 1

            if maximum_index == minimum_index:
                new_list = []
                i = 0
                if maximum_index == 0:
                    new_list = [checked_number]
                    for i in range(len(ordered)):
                        new_list.append(ordered[i])
                elif maximum_index == len(ordered):
                    new_list = ordered
                    new_list.append(checked_number)
                else : 
                    for i in range(maximum_index):
                        new_list.append(ordered[i])
                    new_list.append(checked_number)
                    all_numbers.remove(checked_number)
                    for i in range(maximum_index, len(ordered)):
                        new_list.append(ordered[i])
                ordered = new_list
                checked_number_index = 0
            
        return ordered


not_ordered = []
for i in range(len(updates)):
    add = True
    for j in range(len(rules)):
        if check(updates[i],rules[j]) == False:
            add = False

    if add == False:
        not_ordered.append(updates[i])

ordered =[]
for i in range(len(not_ordered)):
    rules_that_apply = []
    for j in range(len(rules)):
        if rules[j][0] in not_ordered[i] and rules[j][1] in not_ordered[i]:
            rules_that_apply.append(rules[j])
    
    ordered.append(order(not_ordered[i], rules_that_apply))

total = 0
for i in range(len(ordered)):
    total += ordered[i][round(len(ordered[i])//2)]

print(total)
#the answer was 5273
