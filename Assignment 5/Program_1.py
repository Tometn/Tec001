num_list = []

while True:
    INPUT = input(">>>>>>> ")
    if INPUT == "":
        break
    else:
        try:
            num_list.append(float(INPUT))
        except:
            print("Invalid")

if num_list != []:
    num_list.sort(reverse=True)
    print(num_list[0:5])
else:
    print("No numbers")
        