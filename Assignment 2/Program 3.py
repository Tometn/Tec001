import os
def hb_value():
    try:
        while True:
            gender = str(input(f"What is your gender? {os.linesep} M: Male     F: Female {os.linesep} "))
            value = float(input("What is your hemoglobin value (g/l)? "))
            normal = 1
            deficit = 0
            over = 2
            if gender == "F" or gender == "f":
                if 117.0 <= value <= 155.0:
                    print("Your hemoglobin value is normal for a female adult.")
                    return normal
                elif value > 155.0:
                    print("Your hemoglobin value is higher than the standard for a normal female adult.")
                    return over
                else:
                    print("Your hemoglobin value is lower than the standard for a normal female adult.")
                    return deficit
            elif gender == "M" or gender == "m":
                if 134.0 <= value <= 167.0:
                    print("Your hemoglobin value is normal for a male adult.")
                    return normal
                elif value > 167.0:
                    print("Your hemoglobin value is higher than the standard for a normal male adult.")
                    return over
                else:
                    print("Your hemoglobin value is lower than the standard for a normal male adult.")
                    return deficit
            else:
                print("Please enter a valid gender.")
    except ValueError:
            print("Please enter a suitable input.")
    except Exception as e:
            print(f"Error {e} has occurred. Please try again.")


if hb_value() == 1:
    print("No need for further treatment.")
else:
    print("Please check on your doctor immediately.")