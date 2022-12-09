# Import here
from support import txt_to_D_list,txt_to_string,txt_to_2D_list

# Write Code here
def output():
    i,t =   ("input.txt","test_input.txt")
    moves = txt_to_D_list(i)
    result = Rope_Bridge(moves)
    print(result)

#function here
def Rope_Bridge(moves):
    visited_places = 0
    origin = (0,0)
    is_diagonal = False

    directions = {
        'R':(1,0),
        'L':(-1,0),
        'U':(0,1),
        'D':(0,-1),
    }

    head_list = []
    tail_list = []
    
    tail_list.append(origin)
    head_list.append(origin)

    for move in moves:
        direction = move.split(' ')[0]
        step_num = int(move.split(' ')[1])

        for i in range(step_num):
            current_head_x = head_list[-1][0] + directions[direction][0]
            current_head_y = head_list[-1][1] + directions[direction][1]
            head_list.append((current_head_x,current_head_y))

            x_diff = abs(head_list[-1][0] - tail_list[-1][0])
            y_diff = abs(head_list[-1][1] - tail_list[-1][1])
            

            if x_diff + y_diff <= 1:
                is_diagonal = False
                continue

            if x_diff == 1 and  y_diff == 1:
                is_diagonal = True
                continue
            
            if is_diagonal: 
                is_diagonal = False
      


            tail_list.append(head_list[-2])
            


    visited_places = len(set(tail_list))




    return visited_places



# output function
output()