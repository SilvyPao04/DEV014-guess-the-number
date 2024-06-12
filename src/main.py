# Import random module, which is part of Python's standard Library
import random

# Import time module for adding delay
import time 

# Generate a random number between 1 and 100
def random_generated_number():
    return random.randint(1, 100)

# Get user's name
def get_user_name():
    return input("Hello! What's your name? ")

# Explain the game instructions to users
def game_instructions(user_name):
    print(f"\nWelcome to the ultimate 'Guess the Number' game, {user_name}!")
    print("Are you ready to test your guessing skills against me?")
    print("Here's the deal: I've randomly chosen a number between 1 and 100.")
    print("Your challenge is to guess that number!")
    print("But watch out, I'm trying to guess it too! Let's see who gets it right first.")
    print("Get ready to challenge me and may the best guesser win!\n")

# Get the user's guess
def get_user_guess():
    return int(input("Enter your guess: "))

# User guess logic
def check_user_guess(user_guess, number_to_guess):
    if user_guess < number_to_guess:
        print("Too low! Give it another try.")
        return False, "low"
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
        return False, "high"
    else:
        return True, "correct"

# Computer guess logic with learning from user's guesses
def computer_guess(min_val, max_val):
    return random.randint(min_val, max_val)

# Main function to play the game
def play_game(user_name):
    number_to_guess = random_generated_number()
    guesses_of_users = []
    guesses_of_computer = []

    # Initialize the range for the computer's guesses
    min_val, max_val = 1, 100

    while True:
        # User's turn
        print(f"Alright, {user_name}, it's your time to shine!")
        user_guess = get_user_guess()

        correct, feedback = check_user_guess(user_guess, number_to_guess)
        if correct:
            print(f"\nWow, {user_name}! You nailed it! You guessed the number!")
            print("Here are all your guesses:", guesses_of_users)
            break  # Breaks the loop if the number is guessed correctly

        guesses_of_users.append(user_guess)
        
        # Adjust the range for the computer's next guess based on user feedback
        if feedback == "low":
            min_val = max(min_val, user_guess + 1)
        elif feedback == "high":
            max_val = min(max_val, user_guess - 1)

        # Print a separator line
        print("\n" + "-" * 50 + "\n")

        # Computer's turn
        print("Now it's my turn to guess!")
        time.sleep(2)
        computer_guess_val = computer_guess(min_val, max_val)
        print(f"My guess is: {computer_guess_val}")

        correct, feedback = check_user_guess(computer_guess_val, number_to_guess)
        if correct:
            print("\nI got it right! I, the computer, guessed the number!")
            print("Here are all my guesses:", guesses_of_computer)
            break  # Breaks the loop if the computer guesses the number correctly

        guesses_of_computer.append(computer_guess_val)
        
        # Adjust the range for the computer's next guess based on computer feedback
        if feedback == "low":
            min_val = max(min_val, computer_guess_val + 1)
        elif feedback == "high":
            max_val = min(max_val, computer_guess_val - 1)

        # Print a separator line
        print("\n" + "-" * 50 + "\n")

    # Ask the player if they want to play again
    play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        play_game(user_name)  # Restart the game
    else:
        print("\nThanks for playing! See you next time.\n")

def main():
    user_name = get_user_name()  # Get user name once
    game_instructions(user_name)  # Show the instructions once
    play_game(user_name)  # Start the game

if __name__ == "__main__":
    main()
