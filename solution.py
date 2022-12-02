# Import here
from support import txt_to_D_list

# Write Code here
def output():
    input = txt_to_D_list()
    result = Rock_Paper_Scissors(input)
    print(result)

#function here
def Rock_Paper_Scissors(input):
    RPS_score = {
        'X': 0,
        'Y': 3,
        'Z': 6,
    }

    W_D_L = {
        'A0': 3,
        'B0': 1,
        'C0': 2,
        'A3': 1,
        'B3': 2,
        'C3': 3,
        'A6': 2,
        'B6': 3,
        'C6': 1,
    }
    b = 0
    for i in input:
        a = i.split(' ')
        score =  RPS_score[a[1]]
        shape_score =  W_D_L[f'{a[0]+str(score)}'] 
        b += (shape_score + score)

    return b

# output function
output()