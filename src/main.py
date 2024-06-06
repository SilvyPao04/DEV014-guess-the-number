#Import random module, which is part of Python's standard Library
import random

#Generate a random number between 1 and 100
random_generated_number = random.randint(1,100)

print("Welcome to 'Guess the Number' game!")
print("I have generated a random number between 1 and 100.")
print("Can you guess what it is?, Let's start!")

# Initialize the variable to store the user's guess
user_guess = None

#Create a list to store the user's guesses
guesses = []

# Start the loop that will run until the user guesses correctly
while user_guess != random_generated_number:
    # Get the user's guess
    user_guess = int(input("Enter your guess: "))

    #Append the guess to the list of user_guesses
    guesses.append(user_guess)
    
    # Check if the guess is too low, too high, or correct
    if user_guess < random_generated_number:
        print("Too low! Try again.")
    elif user_guess > random_generated_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You won, you guessed the number.")
        print("Here are all your tries:", guesses)

