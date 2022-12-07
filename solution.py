# Import here
from support import txt_to_D_list,txt_to_string
import re
# Write Code here
def output():
    # "input.txt"
    # "test_input.txt"

    terminal_output = txt_to_D_list('test_input.txt')
    result = No_Space_Left_On_Device(terminal_output)
    print(result)

#function here
cwd = root = {}
def No_Space_Left_On_Device(terminal_output):
    stack = []

    for line in terminal_output:
        line = line.strip()
        if line[0] == "$":
            if line[2] == "c":
                dir = line[5:]
                if dir == "/":
                    cwd = root
                    stack = []
                elif dir == "..":
                    cwd = stack.pop()
                else:
                    if dir not in cwd:
                        cwd[dir] = {}
                    stack.append(cwd)
                    cwd = cwd[dir]
        else:
            x, y = line.split()
            if x == "dir":
                if y not in cwd:
                    cwd[y] = {}
            else:
                cwd[y] = int(x)
   
    return solve()[1]

def solve(dir = root):
    if type(dir) == int:
        return (dir, 0)
    size = 0
    ans = 0
    for child in dir.values():
        s, a = solve(child)
        size += s
        ans += a
    if size <= 100000:
        ans += size
    return (size, ans)




# output function
output()