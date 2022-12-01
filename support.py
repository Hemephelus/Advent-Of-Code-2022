def open_file():
    f = open("input.txt", "r")
    return f.read()

def txt_to_string():
    return open_file()

def txt_to_D_list():
    D_List = open_file()
    D_List = D_List.split('\n')
    return D_List