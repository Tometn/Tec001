#Inches to centimeters converter 'til negative number.
try:
    while True:
        inch = float(input("Please enter the value in inches."))
        if inch < 0:
            print('You have entered a negative value.')
            print('Program is stopping.')
            break
        else:
            print(f'Your value is {inch * 2.54} centimeters.')
except Exception as e:
    print("e")