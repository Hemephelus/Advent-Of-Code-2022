def open_file(input):
    f = open(input, "r")
    return f.read()

def txt_to_string(input):
    return open_file(input)

def txt_to_D_list(input):
    D_List = open_file(input)
    D_List = D_List.split('\n')
    return D_List