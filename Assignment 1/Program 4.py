#Sum, product, and average of 3 inputted integers
inter1, inter2, inter3 = map(int, (input("The three integers given are:").split()))
sum = inter1 + inter2 + inter3
product = inter1 * inter2 * inter3
average = (inter1 + inter2 + inter3) / 3
print("The sum is", sum)
print("The product is", product)
print("The average is", average)