"""This is the Ultimate 'Guess the Number' Game"""

import random
import time

def random_generated_number():
    """Generate a random number between 1 and 100"""
    return random.randint(1, 100)

def get_user_name():
    """Prompt the user to enter their name."""
    return input("Hello! What's your name? ")

def game_instructions(user_name):
    """Print game instructions for the 'Guess the Number' game."""
    print(f"\nWelcome to the ultimate 'Guess the Number' game, {user_name}!")
    print("Are you ready to test your guessing skills against me?")
    print("Here's the deal: I've randomly chosen a number between 1 and 100.")
    print("Your challenge is to guess that number!")
    print("But watch out, I'm trying to guess it too! Let's see who gets it right first.")
    print("Get ready to challenge me and may the best guesser win!\n")

def get_user_guess():
    """Prompt the user to enter a guess and validate the input."""
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("Oops! That doesn't look like a valid number.")
            print("Please enter an integer (a whole number).")

# User guess logic
def check_user_guess(user_guess, number_to_guess):
    """Check if the user's guess matches the number to guess."""
    if user_guess < number_to_guess:
        print("Too low! Give it another try.")
        return False, "low"
    if user_guess > number_to_guess:
        print("Too high! Try again.")
        return False, "high"
    return True, "correct"

# Computer guess logic
def computer_guess(min_val, max_val):
    """Generate a random guess for the computer within the specified range."""
    return random.randint(min_val, max_val)

def adjust_range(min_val, max_val, guess, feedback):
    """Adjust the guessing range based on feedback."""
    if feedback == "low":
        min_val = max(min_val, guess + 1)
    elif feedback == "high":
        max_val = min(max_val, guess - 1)
    return min_val, max_val

def play_game(user_name):
    """Main function to play the game."""
    number_to_guess = random_generated_number()
    guesses_of_users = []
    guesses_of_computer = []
    min_val, max_val = 1, 100 # Initialize the range for the computer's guesses
    total_attempts = 0 # Counter of total attempts

    while True:
        # User's turn
        print(f"Alright, {user_name}, it's your time to shine!")
        user_guess = get_user_guess()
        total_attempts += 1

        correct, feedback = check_user_guess(user_guess, number_to_guess)
        guesses_of_users.append(user_guess)

        if correct:
            print(f"\nWow, {user_name}! You nailed it! You guessed the number!")
            print("Here are all your guesses:", guesses_of_users)
            print("Total attempts:", total_attempts)
            break  # Breaks the loop if the number is guessed correctly

        # Adjust the range for the computer's next guess based on user feedback
        min_val, max_val = adjust_range(min_val, max_val, user_guess, feedback)

        # Print a separator line
        print("\n" + "-" * 50 + "\n")

        # Computer's turn
        print("Now it's my turn to guess!")
        time.sleep(2)
        computer_guess_val = computer_guess(min_val, max_val)
        print(f"My guess is: {computer_guess_val}")

        correct, feedback = check_user_guess(computer_guess_val, number_to_guess)
        guesses_of_computer.append(computer_guess_val)

        if correct:
            print("\nI got it right! I, the computer, guessed the number!")
            print("Here are all my guesses:", guesses_of_computer)
            print("Total attempts:", total_attempts)
            break  # Breaks the loop if the computer guesses the number correctly

        # Adjust the range for the computer's next guess based on computer feedback
        min_val, max_val = adjust_range(min_val, max_val, computer_guess_val, feedback)

        # Print a separator line
        print("\n" + "-" * 50 + "\n")

    # Ask the player if they want to play again
    play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        play_game(user_name)  # Restart the game
    else:
        print("\nThanks for playing! See you next time.\n")

def main():
    """Main function to start the 'Guess the Number' game."""
    user_name = get_user_name()  # Get user name once
    game_instructions(user_name)  # Show the instructions once
    play_game(user_name)  # Start the game

if __name__ == "__main__":
    main()
