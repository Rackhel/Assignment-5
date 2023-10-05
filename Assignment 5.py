#Number 1
print("This is Number 1.\n")
while True:
    user_str = input("Please enter two words: ")

    if user_str.lower() == 'done' or not user_str :
        print("Bye !!")
        break    
    
    two_words = user_str.split()

    if len(two_words) != 2:
        print("Please enter two words.")
    else:
        sorted_words = sorted(two_words)
        first, second = sorted_words
        print(f"{first} comes first.")

print("Program terminated.")

print("\n")
#Number 2
print("This is Number 2.\n")
inputs = input("Enter string: ")
print(f"Input string = {inputs}")
inputted = len(inputs)
index = inputted - 1
while index >= 0:
    letter = inputs[index]
    print(letter)
    index = index - 1

print("\n")
#Number 3
print("This Number 3.\n")
string_input = input("Please enter string: ")
numbers = 0
uppercase_letters = 0
lowercase_letters = 0
other_characters = 0
for char in string_input:
    if char.isdigit():
        numbers += 1
    elif char.isupper():
        uppercase_letters += 1
    elif char.islower():
        lowercase_letters += 1
    else:
        other_characters += 1

print("Uppercase Letters: ", uppercase_letters)
print("Lowercase Letters: ", lowercase_letters)
print("Numbers: ", numbers)
print("Other Characters: ", other_characters)

print("\n")
#Number 4
print("This is Number 4.\n")
while True:
    string_string = input("Please enter string: ")
    if string_string.lower() == 'done':
        print("Bye !")
        break

    special_characters = set(":,.!?")
    Changed_string = ''.join(char for char in string_string if char not in special_characters).upper()
    print(Changed_string)

print("Program terminated.")

print("\n")
print("End of Program.")
print("Rackhel, 202312229.")
    

    

