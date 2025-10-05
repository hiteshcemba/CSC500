# Define the secret number
secret_number = 7
# Initialize guess to a value that is not the secret number
guess = 0
# Loop until the correct number is guessed
while guess != secret_number:
    # Prompt user for a guess
    guess_str = input("Guess the secret number: ")
    guess = int(guess_str)
    # Provide feedback to the player
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
# Congratulate the player when the correct number is guessed
print("Congratulations! You guessed the secret number.")