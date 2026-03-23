def ood_num_list_remover(Num_list):
    New_list = []
    for num in Num_list:
        try:
            Num_list[Num_list.index(num)] = int(num)
            if num % 2 == 0:
                New_list.append(num)
        except ValueError:
            return "Invalid list"
    return New_list

#Test program

Test_list = [1.0, 2, 3, 4, 5.0]

print("Before: ", Test_list)
print("After: ", ood_num_list_remover(Test_list))