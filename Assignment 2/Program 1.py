#Zander size limiter
def zander():
    while True:
        try:
            size = int(input("How big is your zander (in centimeters)? "))
            if size < 0:
                print("Please enter a suitable number.")
            elif size >= 100:
                print("That is a BIG zander!")
                break
            elif size >= 42:
                print("Your zander meets the requirements!")
                break
            else:
                print("Your zander doesn't meets the requirements!")
        except ValueError:
            print("Please enter a whole number!")
        except Exception as e:
            print(f"An error has occurred! {e}")
zander()