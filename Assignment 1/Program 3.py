#Perimeter and area of rectangle calculator (from with and length)
import math
from decimal import Decimal, ROUND_HALF_UP
def Round(n):
    rounded_n = Decimal.from_float(n).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    return rounded_n
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
peri = (length + width) * 2
area = length * width
print(f"Area: {area}")
print(f"Perimeter: {peri}")
print(f"Rounded area: {Round(area)}")
print(f"Rounded perimeter: {Round(peri)}")

