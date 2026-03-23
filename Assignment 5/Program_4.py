def sum_int(int_list):
    for num in int_list:
        try:
            int_list[int_list.index(num)] = int(num)
        except ValueError:
            return "Invalid list"

    return sum(int_list)

Test_list = [1, 2, 3.0, 4]

print(sum_int(Test_list))