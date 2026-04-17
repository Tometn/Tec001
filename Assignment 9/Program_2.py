def word_finder(file_open,keyword):
    with open(file_open,'r') as file:
        line_num_list = []
        for index,line in enumerate(file):
            if keyword in line:
                line_num_list.append(index + 1)
        return line_num_list
result = word_finder('some_strings.txt','This')
print(result)