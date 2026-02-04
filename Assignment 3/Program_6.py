#Taking the middle character(s) out of a string

User_str = str(input("Enter your string: "))
if len(User_str) == 0:
    print("Your string is empty.")
elif len(User_str) % 2 == 0:
    print(f"The middle charaters are: {User_str[int(len(User_str) / 2 - 1)]} and {User_str[int((len(User_str) / 2))]}")
else:
    print(f"The middle character is: {User_str[int(((len(User_str) - 1) / 2))]}")