# Import here
from support import txt_to_D_list

# Write Code here
def output():
    pairs = txt_to_D_list()
    result = Camp_Cleanup(pairs)
    print(result)

#function here
def Camp_Cleanup(pairs):
    count = 0
    for pair in pairs:
        c = 0
        p = pair.split(',')
        p1 = p[0].split('-')
        p2 = p[1].split('-')

        for i in range(int(p1[0]),int(p1[1])+1):
            if str(i) in p2:
                count += 1
                c += 1
                break
        for i in range(int(p2[0]),int(p2[1])+1):
            if str(i) in p1:
                count += 1
                c += 1
                break
        if c > 1:
            count -= 1

       
    return count

# output function
output()