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
    max_scenic_score = float('-inf')

    trans_tree_map = [[row[i] for row in tree_map] for i in range(len(tree_map[0]))]

    for i,row in enumerate(tree_map):
        for j,value in enumerate(row):
            if i == 0 or j == 0:
                continue

            if i == len(tree_map)-1 or j == len(row)-1:
                continue
            
            left = calc_num_trees(int(value),tree_map[i][0:j],True)
            right = calc_num_trees(int(value),tree_map[i][j+1:len(row)],False)
            up = calc_num_trees(int(value),trans_tree_map[j][0:i],True)
            down = calc_num_trees(int(value),trans_tree_map[j][i+1:len(tree_map)],False)

            scenic_score = left * right * up * down

            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score

    return max_scenic_score 

def calc_num_trees(value,view_range,is_backward):
    visible_trees = 0
    for i,tree in enumerate(view_range):
        if is_backward:
            j = (i+1) * -1
        else:
            j = i

        if value <= int(view_range[j]):
            visible_trees += 1
            break
        visible_trees += 1

    return visible_trees

# output function
output()