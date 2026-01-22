#Circle's circumference (with rounding)
import math
from decimal import Decimal, ROUND_HALF_UP
radius = float(input("Enter the radius of the circle: "))
circumference = radius * math.pi * 2
print(f"The circumference of the circle is {circumference}!")
decimalCir = Decimal.from_float(circumference)
roundedCir = Decimal(decimalCir.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
print(f"The rounded circumference is {roundedCir}!")
