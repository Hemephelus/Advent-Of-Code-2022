# Import here
from support import txt_to_D_list,txt_to_string,txt_to_2D_list

# Write Code here
def output():
    i,t =   ("input.txt","test_input.txt")
    result = Treetop_Tree_House(t)
    print(result)

#function here
def Treetop_Tree_House(tree_map):
    sum_visible = 0

    for i,row in enumerate(tree_map):
        for j,col in enumerate(row):
            if i == 0 or j == 0:
                sum_visible += 1
                continue

            if i == len(tree_map)-1 or j == len(i)-1:
                sum_visible += 1
                continue

    return sum_visible 

# output function
output()