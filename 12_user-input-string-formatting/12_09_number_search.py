# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

# number = 9

# found = ""

# while found != number:
#     if number in range[:1000000000]:
#             found = number
#     else:
#         continue

# print(found)

while True:
            # Prompt the user to enter a number
            user_input = int(input("Please enter a number between 0 and 1,000,000,000: "))
            
            # Check if the number is within the specified range
            if 0 <= user_input <= 1_000_000_000:
                print(user_input)  # Return the valid number
                False
            else:
                print("The number is not within the range. Please try again.")