# Import here
from support import txt_to_D_list

# Write Code here
def output():
    line = txt_to_D_list()
    result = Calorie_Counting(line)
    print(result)

#function here
def Calorie_Counting(line):
    elve_cal = []
    elve_position = 0

    for l in line:
        if l == '':
            elve_position += 1
            continue
        elve_cal.append(0)
        elve_cal[elve_position] += int(l)

    max_cal = max(elve_cal)

    return max_cal
        




# output function
output()