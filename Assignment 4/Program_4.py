#find and hide phone numbers

import re

def Pho_num_redacter(Text_wall):
    Redactment_list = re.findall(r'\d{10}|\+084\d+ |\+084\s*\d+', Text_wall)
    new_text = Text_wall
    for match in Redactment_list:
        new_text = new_text.replace(match, "[REDACTED]")
    return new_text

while True:
    INPUT = str(input(">>>>> "))
    if INPUT.lower() == "end":   
        break
    else:
        print(Pho_num_redacter(INPUT))