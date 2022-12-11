# Import here
from support import txt_to_D_list,txt_to_string,txt_to_2D_list

# Write Code here
def output():
    i,t =   ("input.txt","test_input.txt")
    instructions = txt_to_D_list(i)
    result = Cathode_Ray_Tube(instructions)
    print(result)

#function here
def Cathode_Ray_Tube(instructions):
    display = '###.....................................'
    CRT = ''
    total_signal_strength = 0
    cycle = 0
    X = []
    x = 1
    j = 0

    for instruction in instructions:
        y = instruction.split(' ')

        if len(y) == 2:
            command, value = y

                
            for a in range(2):
                cycle += 1
                if display[j%40] == '#':
                    CRT += '#'
                if display[j%40] == '.':
                    CRT += '.'
                j += 1
                if cycle%40 == 0:
                    X.append(CRT)
                    CRT = ''

            x += int(value)
            s = x - 1
            display = ''
            for i in range(40):
                if i >= s and i < s+3:
                    display += '#'
                    continue
                display += '.'
            continue

        if display[j%40] == '#':
            CRT += '#'
        if display[j%40] == '.':
            CRT += '.'
        j += 1

        cycle += 1
        if cycle%40 == 0:
            X.append(CRT)
            CRT = ''


    for p in X:
        print(p)
        
    # total_signal_strength = sum(X)
    return total_signal_strength

# output function
output()