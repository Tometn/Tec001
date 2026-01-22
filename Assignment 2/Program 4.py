#Leap year determiner
def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year")
            else:
                print(f"{year} is not a leap year")
        else:
            print(f"{year} is a leap year")
try:
    leap_year(int(input("Enter a year: ")))
except ValueError:
    print("Please enter a valid year")
except Exception as e:
    print(f"Error: {e}")