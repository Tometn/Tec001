def odd_number_remover(list):
    new_list = []
    for item in list:
        if item % 2 == 0:
            new_list.append(item)
    return new_list

num_list = [0, 2, 1, 5, 7, 9, 10]
short_list = odd_number_remover(num_list)
print(num_list)
print(short_list)
