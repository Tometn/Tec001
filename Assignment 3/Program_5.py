# Login logic program
Login_counter = 0
Cor_User = str("python")
Cor_Pass = str("rules")

while True:
    try:
        while True:
            if Login_counter < 5:
                User_ = str(input("Username: "))
                Pass_ = str(input("Password: "))
                if User_ == Cor_User and Pass_ == Cor_Pass:
                    print("Welcome")
                    Login_counter = 0
                    break
                elif User_ != Cor_User or Pass_ == Cor_Pass:
                    Login_counter += 1
                    if Login_counter < 5:    
                        print("Please try again")
                        print(f"You have {5 - Login_counter} attempts left.")
            else:
                print("Access denied")
                break
        break
    except Exception as e:
        print("Error occured: ", e)