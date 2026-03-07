#New name & Existing name (case sensitive)

name_list = set()

def data_repetition_checker(chunk_data, new_member):
    count = 0
    for member in chunk_data:
        if new_member == member:
            count += 1
    if count > 0:
        return True
    else:
        return False
                

while True:
    INPUT = str(input(">>>>  "))
    if INPUT == "":
        break
    if data_repetition_checker(name_list, INPUT):
        print("Existing name")
    else:
        print("New name")
    name_list.add(INPUT)

if name_list != []:
    for name in name_list:
        print(name)
    