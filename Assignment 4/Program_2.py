#Hex colors: #0a1b2c case insensitive

import string

def Hex_Color_checker(color):
    if len(color) != 7:
        return False
    else:
        if color[0] == "#":
            chara_set = color[1:]
            for character in chara_set:
                if character.lower() in string.ascii_lowercase or character in string.digits:
                    continue
                else:
                    return False
            return True
        
while True:
    INPUT = str(input(">>>>> "))
    if INPUT.lower() == "end":   
        break
    else:
        print(Hex_Color_checker(INPUT))
