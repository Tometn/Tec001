


def uppercase(file_open):
    with open(file_open,'r') as file:
        content = file.read()
    with open('output.txt','w') as outfile:
        outfile.write(content.upper())

uppercase('some_strings.txt')