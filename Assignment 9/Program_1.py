

def count_line(file_open):
    count = 0
    with open(file_open,'r') as file:
        for line in file:
            if line.strip() !='':
                count += 1
    return count


result = count_line('some_strings.txt')
print(result)