import random

print("Welcome to number guessing game.\n")
while True:
    print("Select a difficulty level:")
    print("1.Easy (1-5)")
    print("2.Medium (1-10)")
    print("3.Hard (1-20)")
    level = int(input("Enter the level number:"))

    if level == 1:
        print("You have selected Easy level.")
        right_number = random.randint(1,5)
    elif level == 2:
        print("You have selected Medium level.")
        right_number = random.randint(1,10)
    else:
        print("You have selected Hard level.")
        right_number = random.randint(1,20)
    print("I've picked a number for you to guess.")


    guessed_number = int(input("Guess a number: "))
    # start loop to continue until user guesses correctly.
    while guessed_number != right_number:
        if   level == 1 and guessed_number == right_number:
            print("Correct guess!!")
            print("You won. Thank you for playing!!")
        elif level == 2 and guessed_number == right_number:
            print("Correct guess!!")
            print("You won. Thank you for playing!!")
        elif level == 3 and guessed_number == right_number:
            print("Correct guess!")
            print("You won!! Thank you for playing!!")
        elif level == 1 and (guessed_number > right_number):
            print("Invalid guess. please enter a smaller number.")
            print("Give it another shot!")
        elif level == 1 and (guessed_number < right_number):
            print("Invalid guess. please enter a bigger number.")
            print("Give it another shot!")
        elif level == 2 and (guessed_number > right_number):
            print("Invalid guess. Please enter a smaller number.")
            print("Give it another shot!")
        elif level == 2 and (guessed_number < right_number):
            print("Invalid guess. please enter a bigger number.")
            print("Give it another shot!")
        elif level == 3 and (guessed_number > right_number):
            print("Invalid guess. Please enter a smaller number.")
            print("Give it another shot.")
        elif level == 3 and (guessed_number < right_number):
            print("Invalid guess. Please enter a bigger number.")
            print("Give it another shot.")
        guessed_number = int(input("Enter guess number again: "))

    print("\nCorrect guess!!")
    print("You won!! Thank you for playing!!")
    print("The number was:" , right_number)
    play_again = input("Play again? (y/n): ").strip().lower()
    if play_again == "y":
        print("Restarting game!!\n")
    else:
        print("Thank you for playing!!")
        break


