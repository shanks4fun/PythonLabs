# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

words = input("Please type 3 words for me so we can figure out which one is the longest: ").lower()


my_list = words.split()
longest = max(my_list, key=len)
length = len(longest)
print(f"{length}, {longest}")