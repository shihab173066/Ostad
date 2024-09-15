"""
(Project 2): Number Guessing Game
OVERVIEW
In this assignment, you will create a CLI-based Number Guessing Game using Python. The
objective of this project is to design an interactive game where the computer selects a
random number between 1 and 100, and the user attempts to guess it. Your program will
need to generate a random number, handle user input, and provide feedback based on the
user's guesses.
TASKS
1. Random Number Generation: Begin by generating a random number within the
range of 1 to 100. This number will serve as the target that the user needs to guess.
The random number should be kept secret from the user until they correctly guess it.
2. Implement User Input Handling: Prompt the user to input their guess and ensure
the input is converted to an integer to compare it with the randomly generated
number. Handle any potential input errors.
3. Loops: Utilize a loop to continuously prompt the user for their guess until they
correctly identify the number. This loop should repeat until the user's guess matches
the randomly selected number, allowing them to keep guessing as many times as
needed.
4. Conditional Logic: After each guess, provide feedback to the user on whether their
guess is too high, too low, or correct. Use conditional logic to compare the user's
guess with the random number and determine which of the three possible outcomes
applies. This feedback should guide the user towards the correct answer.
5. Ending the Game: Once the user successfully guesses the number, conclude the
game by printing a congratulatory message. Additionally, inform the user of the
number of attempts it took them to guess the number correctly. This helps in
providing a sense of achievement and closure to the game.


SAMPLE INPUT OUTPUT:
Welcome to the Number Guessing Game!
Try to guess the number between 1 and 100.

Enter your guess: 50
Too low!

Enter your guess: 75
Too high!

Enter your guess: 62
Too low!

Enter your guess: 68
Congratulations! You've guessed the number in 4 attempts.

NOTE:
1. Ensure the program can handle invalid inputs, such as non-numeric values, gracefully.
2. Implement meaningful error messages for invalid operations, such as division by zero.
"""

import random

# Function for guessing game
def guessing_game():
    
    target_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Shihab's Number Guessing Game!")
    print("Try to guess the number between 1 and 100.")

    # Recursive function to handle the guessing process
    def guess_number():
        nonlocal attempts
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            if user_guess < target_number:
                print("Oh no! Too low!")
                guess_number()  
            elif user_guess > target_number:
                print("Oh! Too high!")
                guess_number()  
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            guess_number()  

    guess_number()

    play_again = input("Do you want to play again? (y / or any character button): ").lower()
    if play_again == "y":
        guessing_game()  # recursion to restart the game if user wishes
    else:
        print("Thank you for playing!")

# Game Start !
guessing_game()
