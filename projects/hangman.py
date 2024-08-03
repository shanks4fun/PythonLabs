# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.

# Hard-code a word that needs to be guessed in the script

# Print an explanation to the user

# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"

# Ask for user input

# Allow only single-character alphabetic input

# Create a counter for how many tries a user has

# Keep asking them for their guess until they won or lost

# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"

# Display a winning message and the full word if they win

# Display a losing message and quit the game if they don't make it


word = "h e l l o"
hiddenWord = "_ _ _ _ _"
guess = ""
attempts = 6
indices = []
word_list = list(hiddenWord)

print ('''Hangman is a classic word-guessing game played with the following rules:

Objective: Guess the hidden word before running out of attempts. (6 attempts)
       
Gameplay:
-The guesser suggests letters one at a time.
-If the guessed letter is in the word, the letter or letters are revealed. 
-If the guessed letter is not in the word, you lose one of your 6 attemps.

Winning and Losing:
-The guesser wins by correctly guessing all the letters in the word before running out of attemps.
-The guesser loses if there are 0 attempts left before the word is guessed.''')

while attempts != 0 and hiddenWord.find("_") != -1:
    print(f"\nHere is your word {hiddenWord}")
    guess = input("\nUsing a single letter, what is your first guess? ").lower()
    if word.find(guess) != -1:
        indices = [index for index, char in enumerate(word) if char == guess]
        for index in indices:
            word_list[index] = guess
            hiddenWord = ' '.join(word_list)
            if hiddenWord.find("_") == -1:
                print("\nCongrats, you are a winner!")
            else:
                continue
    else:
        attempts -= 1
        if attempts == 0:
            print("\nGAME OVER")
            break
        else:
            print(f"Nope, {attempts} attempt(s) left.")
