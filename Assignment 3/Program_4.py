#User guessing game (1-10, intergers only)
import random


#Defining function
def higher_or_lower(guess, rn):
    if guess < rn:
        return ">Higher"
    elif guess > rn:
        return ">Lower"
    else:
        return ">You got it!"

#Assigning variables
user_guess_count = 0
fixed_rn = random.randint(1, 10)


#user's first guess
while True:
    try:
        user_guess = (int(input("Enter your guess between 1 and 10: ")))
        break
    except ValueError:
        print("Invalid number, please try again.")
    except Exception as e:
        print("Error: ", e, "Please try again") 


# guess counter + next guesses
print(higher_or_lower(user_guess, fixed_rn))
while True:
    try:
        while user_guess != fixed_rn:
            user_guess = (int(input("Try again: ")))
            user_guess_count += 1
            print(higher_or_lower(user_guess, fixed_rn))
        user_guess_count += 1
        print(f"Congratulations! You've guessed <<  {user_guess_count}  >> times.")
        break
    except Exception as e:
        print("Error: ", e, "Please try again")
