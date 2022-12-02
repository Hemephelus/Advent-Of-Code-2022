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
        'X': 1,
        'Y': 2,
        'Z': 3,
    }

    W_D_L = {
        'A X': 3,
        'B X': 0,
        'C X': 6,
        'A Y': 6,
        'B Y': 3,
        'C Y': 0,
        'A Z': 0,
        'B Z': 6,
        'C Z': 3,
    }
    b = 0
    for i in input:
      a =  W_D_L[i] + RPS_score[i.split(' ')[1]]
      b += a

    return b

# output function
output()