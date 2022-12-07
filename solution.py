# # Import here
from support import txt_to_D_list,txt_to_string
# import re
# # Write Code here
# def output():
#     # "input.txt"
#     # "test_input.txt"

#     terminal_output = txt_to_D_list('input.txt')
#     result = No_Space_Left_On_Device(terminal_output)
#     print(result)

# #function here
# cwd = root = {}
# def No_Space_Left_On_Device(terminal_output):
#     stack = []

#     for line in terminal_output:
#         line = line.strip()
#         if line[0] == "$":
#             if line[2] == "c":
#                 dir = line[5:]
#                 if dir == "/":
#                     cwd = root
#                     stack = []
#                 elif dir == "..":
#                     cwd = stack.pop()
#                 else:
#                     if dir not in cwd:
#                         cwd[dir] = {}
#                     stack.append(cwd)
#                     cwd = cwd[dir]
#         else:
#             x, y = line.split()
#             if x == "dir":
#                 if y not in cwd:
#                     cwd[y] = {}
#             else:
#                 cwd[y] = int(x)
   
#     return solve()

# def size(dir = root):
#     if type(dir) == int:
#         return dir
#     return sum(map(size, dir.values()))

# t = size() - 40_000_000

# def solve(dir = root):
#     ans = float("inf")
#     if size(dir) >= t:
#         ans = size(dir)
#     for child in dir.values():
#         if type(child) == int:
#             continue
#         q = solve(child)
#         ans = min(ans, q)
#     # print(ans)
#     return ans




# # output function
# output()


cwd = root = {}
stack = []
input = txt_to_D_list('input.txt')
for line in input:
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

def size(dir = root):
    if type(dir) == int:
        return dir
    return sum(map(size, dir.values()))

t = size() - 40_000_000

def solve(dir = root):
    ans = float("inf")
    if size(dir) >= t:
        ans = size(dir)
    for child in dir.values():
        if type(child) == int:
            continue
        q = solve(child)
        ans = min(ans, q)
    return ans

print(solve())