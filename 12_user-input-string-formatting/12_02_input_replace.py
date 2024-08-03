# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

symbol = ""
sentance = ""

sentance = input("Please type a string of words for me: ").lower()
symbol = input("Please enter 1 symbol for me: ")

newSentance = sentance.replace(sentance[0],symbol)
print(newSentance)


