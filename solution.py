from support import txt_to_string


def output():
    brackets = txt_to_string()
    print(type(brackets))
    result = Not_Quite_Lisp(brackets)
    print(result)

def Not_Quite_Lisp(brackets):
    dict ={
        "(" : 1,
        ")" : -1,
    }
    t = 0
    
    for b in brackets:
        t += dict[b]

    return t
        




# output function
output()