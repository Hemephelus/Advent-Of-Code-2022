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
    for Rucksack in Rucksacks:
        half = int(len(Rucksack)/2)
        compartment_A = Rucksack[0:half]    
        compartment_B = Rucksack[half:]
        unique_list = set(compartment_A)
     
        for letter in unique_list:
            position = compartment_B.find(letter)
            if position >= 0:
                if letter.isupper():
                    item_value = items[letter.lower()]
                    item_value += 26
                else:
                    item_value = items[letter]
                               
                total += item_value

            
    return total

# output function
output()