#Highlight initials of each word in a string
Sent = str(input("Please enter your sentence: "))
print("The acronym of your sentence is:", "".join(word[0] for word in Sent.split()).upper())