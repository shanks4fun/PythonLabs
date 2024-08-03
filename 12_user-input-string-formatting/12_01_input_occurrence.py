# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

string = "hello world"

userinput = input("Type in any single digit letter to see where or even if it exists in the secret word: ").lower()

if len(userinput) != 1 or userinput.isalpha() == False:
    print("A single alpha character is required.")
else:
    charPosition = string.find(userinput)
    if charPosition == -1:
        print("Your letter isn't in the secret phrase :(")
    else:
        print("Your letter is in position",charPosition, "of the secret word!")


