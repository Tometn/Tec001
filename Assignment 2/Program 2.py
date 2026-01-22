# Cabin class information query?
import os
def class_info():
    while True:
        try:
            class_ = str(input(f" For description of cabin class, please enter the corresponding: {os.linesep} LUX: Luxury class {os.linesep} A: A class {os.linesep} B: B class {os.linesep} C: C class {os.linesep} "))
            if class_ == "LUX":
                print("Luxury class is on the upper-deck cabin with a balcony for each cabin.")
                break
            elif class_ == "A":
                print("A class is above the car deck, and each cabin is equipped with a window.")
                break
            elif class_ == "B":
                print("B class cabins are windowless cabins ABOVE the car deck.")
                break
            elif class_ == "C":
                print("C class cabins are windowless cabins BELOW the car deck.")
                break
            else:
                print(os.linesep, "INVALID CABIN CLASS", os.linesep)
        except Exception as e:
            print(f"Error {e} occurred")
class_info()