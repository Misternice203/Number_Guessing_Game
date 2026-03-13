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
    counted_guesses = 1

    while guessed_number != right_number:
        if guessed_number > right_number:
            print("Invalid guess. Please enter a smaller number.")
        else:
            print("Invalid guess. Please enter a bigger number.")
        print("Give it another shot!")
        guessed_number = int(input("Guess a number: "))
        counted_guesses += 1

    print("\nCorrect guess!!")
    print("You guessed the number in", counted_guesses, "guesses.")
    print("You won!! Thank you for playing!!")
    print("The number was:" , right_number)
    play_again = input("Play again? (y/n): ").lower()
    if play_again == "y":
        print("Restarting game!!\n")
    else:
        print("Thank you for playing!!")
        break

