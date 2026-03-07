#Seasons

Seasons = ("spring", "summer", "autumn", "winter")

try:
    Month_input = int(input(">>>> "))
    if Month_input <= 0 or Month_input > 12:
        print("Invalid month")
    elif Month_input > 11 or Month_input <= 2:
        print(Seasons[3])
    elif Month_input > 2 and Month_input <= 5:
        print(Seasons[0])
    elif Month_input > 5 and Month_input <= 8:
        print(Seasons[1])
    else:
        print(Seasons[2])
except ValueError:
    print("Invalid month")
