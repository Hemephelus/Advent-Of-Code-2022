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
    v = set([(0, 0)])
    directions = {
        'R':(1,0),
        'L':(-1,0),
        'U':(0,1),
        'D':(0,-1),
    }

    rope = []
    R = [[0, 0] for _ in range(10)]

    for i in range(10):
        rope.append([])
        rope[i].append(origin)


    for move in moves:
        direction = move.split(' ')[0]
        step_num = int(move.split(' ')[1])

        for i in range(step_num):

            current_head_x = rope[0][-1][0] + directions[direction][0]
            current_head_y = rope[0][-1][1] + directions[direction][1]

            R[0][0] += current_head_x
            R[0][1] += current_head_y

            # rope[0].append((current_head_x,current_head_y))

            for j in range(9):
                H = R[j]
                T = R[j + 1]
               
                x_diff = H[0] - T[0]
                y_diff = H[1] - T[1]

                if abs(x_diff) > 1 or abs(y_diff) > 1:
                    if x_diff == 0:
                        T[1] += y_diff // 2
                    elif y_diff == 0:
                        T[0] += x_diff // 2
                    else:
                        T[0] += 1 if x_diff > 0 else -1
                        T[1] += 1 if y_diff > 0 else -1
        
            # rope[j+1].append(rope[j][-2])
            v.add(tuple(R[-1]))
        # print(rope)
        # return
            


    visited_places = len(v)




    return visited_places



# output function
output()