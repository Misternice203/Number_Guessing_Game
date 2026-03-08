import random

print("Welcome to number guessing game.")
right_number = random.randint(1,5)

print("I've picked a number for you to guess.")
print("The number is between 1 and 5.")

guessed_number = int(input("Guess a number: "))

while guessed_number != right_number:
    if guessed_number == right_number:
        print("Correct guess.")
    elif guessed_number > right_number:
        print("Your guess is not correct.")
        print("Give it another shot.")
        print("Choose a lower number.")
    elif guessed_number < right_number:
        print("Your guess is not correct.")
        print("Give it another shot.")
        print("Choose a higher number.")
    else:
        print("Incorrect guess.")
    guessed_number = int(input("Enter guess number again: "))

print("Congratulations! You've guessed the right number.")

