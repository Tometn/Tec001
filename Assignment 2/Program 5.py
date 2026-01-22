#Pizza program
#the calculator
def pizza_value_calculator(dia, price):
    radius = dia / 2
    area = radius ** 2
    price_to_area = price / area
    return price_to_area
#main program
try:
    dia1, price1 = float(input("Please enter the diameter and price of the first pizza (in centimeters and US dollars): "))
    dia2, price2 = float(input("Please enter the diameter and price of the second pizza (in centimeters and US dollars): "))
    if pizza_value_calculator(dia1, price1) > pizza_value_calculator(dia2, price2):
        print(f"Your second pizza has a better value at {pizza_value_calculator(dia2, price2)} USD per centimeters square")
    elif pizza_value_calculator(dia1, price1) < pizza_value_calculator(dia2, price2):
        print(f"Your first pizza has a better value at {pizza_value_calculator(dia1, price1)} USD per centimeters square")
    else:
        print(f"Both of your pizzas has the same value at {pizza_value_calculator(dia2, price2)} USD per centimeters square")

except ValueError:
    print("Please enter a suitable value for diameter and price")
except Exception as e:
    print(f"Error: {e}")