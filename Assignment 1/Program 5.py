#Convert the sum of talent, pounds, and lots into Kilograms and grams

talent = int(input("Talent(s): "))
pound = int(input("Pound(s): "))
lot = int(input("Lot(s): "))
#convert to grams
sum_grams =  13.3*(lot + 32 * (pound + 20*talent))
print(f"The sum of the three mass in medieval units is {sum_grams // 1000} kilograms and {round(sum_grams % 1000)} grams.")