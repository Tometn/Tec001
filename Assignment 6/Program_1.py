#Append to list and sort

Num_list = []

while True:
    INPUT = input(">>>>> ")
    if INPUT == "":
        break
    else:    
        try:
            Num_list.append(float(INPUT))
        except ValueError:
            print("Invalid number")

Num_list.sort(reverse=True)

print(Num_list)