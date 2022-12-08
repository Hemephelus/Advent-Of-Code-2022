# Import here
from support import txt_to_D_list,txt_to_string,txt_to_2D_list

# Write Code here
def output():
    i,t =   ("input.txt","test_input.txt")
    tree_map = txt_to_2D_list(i)
    result = Treetop_Tree_House(tree_map)
    print(result)

#function here
def Treetop_Tree_House(tree_map):
    sum_visible = 0
    trans_tree_map = [[row[i] for row in tree_map] for i in range(len(tree_map[0]))]

    for i,row in enumerate(tree_map):
        for j,value in enumerate(row):
            if i == 0 or j == 0:
                sum_visible += 1
                continue

            if i == len(tree_map)-1 or j == len(row)-1:
                sum_visible += 1
                continue

            if int(value) <= int(max(tree_map[i][0:j])) and int(value) <= int(max(tree_map[i][j+1:len(row)])) and int(value) <= int(max(trans_tree_map[j][0:i]))  and int(value) <= int(max(trans_tree_map[j][i+1:len(tree_map)])):
                continue
            else:
                sum_visible += 1

    return sum_visible 

# output function
output()