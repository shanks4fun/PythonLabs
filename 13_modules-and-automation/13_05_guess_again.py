# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.

import random

num = random.randint(1,100)
attempt = 5
print("Guess a number between 1 and 100 within 5 guesses to win.")
guess = 0



while attempt > 0:
    guess = (input("\nEnter a number from 1 to 100: "))
    if guess.lower() == "exit":
        break
    elif guess.isdigit() == False:
        print("Your guess must be a number")
        continue
    else:
        guess = int(guess)
        attempt -= 1
       
        if guess == num:
            print("Nicely done, you win!")
            break
        elif guess < num:
            print("nope, go higher")
        else:
            print("nope, go lower")

