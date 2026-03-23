while True:
    div = 2
    count = 0
    try:    
        INPUT = input(">>>")
        if INPUT == "":
            break
        else:
            INPUT = int(INPUT)
    except ValueError:
        print("Invalid")
    while True:
        if div <= INPUT ** 0.5 and count == 0:
            if INPUT % div == 0:
                count += 1
            else:
                div += 1
        else:
            break
    if count == 0:
        print("Prime number")
    else:
        print("Not a prime number")
