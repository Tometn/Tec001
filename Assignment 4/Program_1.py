#A course code has the format of 3 uppercase letters and 3 digits


def Cour_format_checker(code):
    if len(code) != 6:
        return False
    else:
        First_3 = code[:3]
        Last_3 =code[3:]
        if First_3 == First_3.upper():
            try:
                int(Last_3)
                return True
            except:
                return False
        else:
            return False



while True:
    INPUT = str(input(">>>>> "))
    if INPUT.lower() == "end":   
        break
    else:
        print(Cour_format_checker(INPUT))

