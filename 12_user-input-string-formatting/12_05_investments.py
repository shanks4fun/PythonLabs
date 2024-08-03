# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

print("Welcome, and thank you for allowing us to help you secure your future.")
amount = float(input("\nPlease enter your investment amount:  "))
rate = float(input("\nPlease enter your yearly interest rate in percentage:  "))
years = int(input("\nPlease enter the amount of years you are looking to invest for:  "))
itera = 0
while years != 0:
   itera += 1
   years -= 1
   interest = (rate * .01) * amount
   amount = interest + amount
   print("Year ",itera," ",amount)