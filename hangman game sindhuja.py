import random

# Predefined list of words
words = ["apple", "banana", "cherry", "date", "elderberry", "sindhuja","bhayya"]

# Select a random word from the list
word = random.choice(words)

# Set the number of incorrect guesses allowed
max_guesses = 5

# Initialize the number of incorrect guesses
guesses = 0

# Initialize the blank spaces for the word
blanks = ["_"] * len(word)

while True:
    # Get the player's guess
    guess = input("Guess a letter: ")

    # Check if the guess is in the word
    if guess in word:
        # Fill in the corresponding blanks
        for i, letter in enumerate(word):
            if letter == guess:
                blanks[i] = guess
    else:
        # Increment the number of incorrect guesses
        guesses += 1

    # Check if the game is over
    if guesses >= max_guesses:
        print("Game Over! The word was", word)
        break
    elif "_" not in blanks:
        print("Congratulations! You guessed the word", word)
        break

    # Print the current state of the word
    print(" ".join(blanks))