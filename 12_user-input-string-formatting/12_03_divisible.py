# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

number = int(input("Give me a number between 1 and 1,000,000,000"))
if number % 3 == 0:
    print("That was a good one, 3 goes into it perfectly!")
    
else:
    print("Sadly not the caliber of number I was looking for :(")