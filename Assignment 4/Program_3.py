#Adding all numbers in a string
#Problems: picking out numbers, e.g: "xa205op" or "add TY564", needs to pick out 205 and 564, not 2, 0 and 5
#Integers only
import string

def Number_summer(sentence):
    words_split = sentence.split()
    list_of_numbers = []
    for index, character in enumerate(words_split):
        if character in string.digits:
            temp_digit_list.append(character)
            try:    
                if words_split[index + 1] in string.digits:
                    continue
                else:
                    list_of_numbers.append(int("".join(temp_digit_list)))
                    temp_digit_list = []
            except IndexError:
                list_of_numbers.append(int("".join(temp_digit_list)))
                temp_digit_list = []
    return sum(list_of_numbers)

while True:
    INPUT = str(input(">>>>> "))
    if INPUT.lower() == "end":   
        break
    else:
        print(Number_summer(INPUT))