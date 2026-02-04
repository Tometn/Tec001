#Numbers into list (stopping with blank) and sorting from low and high.
user_input_list = []
while True:
    try:
        while True:
            num = str(input('> '))
            if num == "" :
                break
            user_input_list.append(float(num))
            print("Added", num)
        break
    except Exception as e:
        print("Error: ", e)
Comp_high = user_input_list[0]
Comp_low = user_input_list[0]
for n in user_input_list:
    if n > Comp_high:
        Comp_high = n
    if n < Comp_low:
        Comp_low = n
