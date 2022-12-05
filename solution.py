# Import here
from support import txt_to_D_list

# Write Code here
def output():
    rearrange_steps = txt_to_D_list()
    result = Supply_Stacks(rearrange_steps)
    print(result)

'''
        [H]     [W] [B]            
    [D] [B]     [L] [G] [N]        
[P] [J] [T]     [M] [R] [D]        
[V] [F] [V]     [F] [Z] [B]     [C]
[Z] [V] [S]     [G] [H] [C] [Q] [R]
[W] [W] [L] [J] [B] [V] [P] [B] [Z]
[D] [S] [M] [S] [Z] [W] [J] [T] [G]
[T] [L] [Z] [R] [C] [Q] [V] [P] [H]
 1   2   3   4   5   6   7   8   9  
'''
#function here
def Supply_Stacks(rearrange_steps):
    
    starting_stacks = {
    '1': ['P','V','Z','W','D','T'],
    '2': ['D','J','F','V','W','S','L'],
    '3': ['H','B','T','V','S','L','M','Z'],
    '4': ['J','S','R'],
    '5': ['W','L','M','F','G','B','Z','C'],
    '6': ['B','G','R','Z','H','V','W','Q'],
    '7': ['N','D','B','C','P','J','V'],
    '8': ['Q','B','T','P'],
    '9': ['C','R','Z','G','H'],
        }

    top_stacks = ''

    for step in rearrange_steps:
        step_to_num = [ int(i) for i in step.split() if i.isdigit()]
        move_num = step_to_num[0]
        from_num = step_to_num[1]
        to_num = step_to_num[2]

        from_stack = starting_stacks[f'{from_num}']

        stacks_moved = from_stack[0:move_num]
        del from_stack[0:move_num]

        starting_stacks[f'{from_num}'] = from_stack
        starting_stacks[f'{to_num}'] = list(reversed(stacks_moved))  + starting_stacks[f'{to_num}']


    for i in range(len(starting_stacks)):
        is_empty = len(starting_stacks[f'{i+1}'])

        if is_empty > 0:
            top_stacks += starting_stacks[f'{i+1}'][0]

    return top_stacks


# output function
output()