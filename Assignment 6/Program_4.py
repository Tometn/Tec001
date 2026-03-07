#Word repetition counter (case insensitive)

Word_dictionary_and_repetion = {}

Text_wall = str(input(">>>>> "))
for word in Text_wall.split():
    word = word.lower()
    if word not in Word_dictionary_and_repetion:
        Word_dictionary_and_repetion[word] = 1
    elif word in Word_dictionary_and_repetion:
        Word_dictionary_and_repetion[word] = Word_dictionary_and_repetion[word] + 1

Desired_word = str(input("Enter the word to find: "))

print(f"The repetition of '{Desired_word}' is {Word_dictionary_and_repetion[Desired_word]} times")