# Import here
from support import txt_to_D_list

# Write Code here
def output():
    Rucksacks = txt_to_D_list()
    result = Rucksack_Reorganization(Rucksacks)
    print(result)

#function here
def Rucksack_Reorganization(Rucksacks):
    total = 0
    group = []
    item_count = {}
    items = {
        'a' : 1,
        'b' : 2,
        'c' : 3,
        'd' : 4,
        'e' : 5,
        'f' : 6, 
        'g' : 7, 
        'h' : 8, 
        'i' : 9, 
        'j' : 10, 
        'k' : 11, 
        'l' : 12, 
        'm' : 13, 
        'n' : 14, 
        'o' : 15, 
        'p' : 16, 
        'q' : 17, 
        'r' : 18, 
        's' : 19, 
        't' : 20, 
        'u' : 21, 
        'v' : 22, 
        'w' : 23, 
        'x' : 24, 
        'y' : 25, 
        'z' : 26, 
    }
    for i, Rucksack in enumerate(Rucksacks):
        unique_list = list(set(Rucksack))

        for letter in unique_list:

            if item_count.get(letter) == None:
                item_count[letter] = 0

            item_count[letter] += 1

            if item_count[letter] >= 3:
                if letter.isupper():
                    item_value = items[letter.lower()] + 26
                
                else:
                    item_value = items[letter]
                total += item_value
        print(item_count)
        if i % 3 == 2:
            item_count = {}
            
                               

            
    return total

# output function
output()