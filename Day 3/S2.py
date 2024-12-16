with open("C:/Users/dmlam/Desktop/AOC2024 D-3.txt","r") as file:
    content = file.read()
print(content)
print(len(content))
possible_char = ["m","u","l","(",",",")","0","1","2","3","4","5","6","7","8","9"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
stages = ["m","u","l","(","numbers",",","numbers",")"]
enabler_stages = ["d","o","(",")"]
current_enabler_stage = -1
disabler_stages = ["d","o","n","'","t","(",")"]
current_disabler_stage = -1
current_stage = -1
first_number = ""
second_number = ""
total = 0
current_state = True

for i in range(len(content)):
    char = content[i]
    if char not in enabler_stages:
        current_enabler_stage = -1
    else :
        if char == enabler_stages[current_enabler_stage + 1]:
            current_enabler_stage += 1
            if current_enabler_stage == 3:
                current_state = True
                current_enabler_stage = -1
        else :
            current_enabler_stage = -1

    if char not in disabler_stages:
        current_disabler_stage = -1
    else :
        if char == disabler_stages[current_disabler_stage + 1]:
            current_disabler_stage += 1
            if current_disabler_stage == 6:
                current_state = False
                current_disabler_stage = -1
        else :
            current_disabler_stage = -1

    if char not in possible_char:
        first_number = ""
        second_number = ""
        current_stage = -1
    else :
        if char == "m":
            first_number = ""
            second_number = ""
            current_stage = 0
        else : 
            if char in numbers:
                if current_stage == 4:
                    first_number += char
                elif current_stage == 3 :
                    current_stage += 1
                    first_number += char
                elif current_stage == 6:
                    second_number += char
                elif current_stage == 5:
                    second_number += char
                    current_stage += 1
            else :
                if char == stages[current_stage + 1]:
                    current_stage += 1
                else :
                    first_number = ""
                    second_number = ""
                    current_stage = -1
                if current_stage == 7:
                    if first_number == "" or second_number == "" or current_state == False:
                        first_number = ""
                        second_number = ""
                        current_stage = -1
                    else : 
                        total += int(first_number) * int(second_number)
                        first_number = ""
                        second_number = ""
                        current_stage = -1
print(total)
#the answer was 72948684
