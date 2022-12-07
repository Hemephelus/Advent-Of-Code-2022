# Import here
from support import txt_to_D_list,txt_to_string

# Write Code here
def output():
    # "input.txt"
    # "test_input.txt"

    terminal_output = txt_to_D_list('test_input.txt')
    result = No_Space_Left_On_Device(terminal_output)
    print(result)

#function here
def No_Space_Left_On_Device(terminal_output):
    space_sum = 0
    base_root = {'main_root':{}}
    list_of_folders = ['main_root']
    
    for line in terminal_output:
        print(base_root['main_root'])
        current_folder = list_of_folders[-1]
        if line == '$ cd /':
            list_of_folders = ['main_root']
            continue
        
        # print(list_of_folders)
        if line == '$ cd ..':
            list_of_folders.pop()
            continue

        if '$ cd' in line:
            new_folder = line.split(' ')[2]
            list_of_folders.append(new_folder)
            continue

        if line == '$ ls':
            continue

        ls_command(line,base_root,list_of_folders)
        # print(current_folder)
    print(base_root['main_root']['a']['e'])
    return space_sum

def ls_command(line,base_root,list_of_folders):
    if 'dir' in line:
        key_name = line.split(' ')[1]
        current_folder = enter_folders(base_root,list_of_folders)
        # ls_command(line,main_root,list_of_folders)
        current_folder[key_name] = {}
    else:
        key_name = line.split(' ')[1]
        current_folder = enter_folders(base_root,list_of_folders)
        current_folder[key_name] = int(line.split(' ')[0])


def enter_folders(base_root,list_of_folders):
    l = base_root
    for folder in list_of_folders:
        l[folder] = l
        # print(l)
    
    return l



# output function
output()