# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.

number = int(input("Type in a number between 1 and 12: "))

Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

if 1 <= number <= 12:
          print(Months[number-1])      
else:
        print("The number is not between 1 and 12. Please try again.")