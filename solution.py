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
    total_signal_strength = 0
    cycle = 0
    X = []
    x = 1
    i = 0
    for instruction in instructions:
        y = instruction.split(' ')

        if len(y) == 2:
            command, value = y

            for a in range(2):
                cycle += 1
                if cycle == (i*40)+20:
                    X.append(x*((i*40)+20))
                    i += 1

            x += int(value)
            continue
    
        if cycle == (i*40)+20:
            X.append(x*((i*40)+20))
            i += 1
        cycle += 1

        if len(X) == 6:
            break

        
    total_signal_strength = sum(X)
    return total_signal_strength

# output function
output()