def open_file(input):
    f = open(input, "r")
    return f.read()

def txt_to_string(input):
    return open_file(input)

def txt_to_D_list(input):
    D_List = open_file(input)
    D_List = D_List.split('\n')
    return D_List

def txt_to_2D_list(input):
    D_List = txt_to_D_list(input)
    List_2D = []
    for i in range(len(D_List)):
        List_2D.append([])
        for j in D_List[i]:
            List_2D[i].append(j)
    return List_2D

def transpose_2d_list(input):
    return [[row[i] for row in input] for i in range(len(input[0]))]