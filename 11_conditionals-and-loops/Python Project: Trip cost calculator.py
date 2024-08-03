# Specifications

# Receive the following arguments from the user:

# Kilometers to drive
# Liters-per-kilometer usage of the car
# Price per liter of fuel
# Calculate the cost of the trip and display it to the user in the console. Apply some of the string formatting 
# tricks that you learned about in this course section.

distance = float(input("Enter the distance you plan to drive in kilometers: "))
literPerKilo = float(input("Enter how many liters per kilometer you car gets: "))
fuelCost = float(input("Enter the current cost for a liter of fuel: "))


tripCost = (fuelCost/literPerKilo) * distance

print(f'''Driving {distance} Kilometers with a car that gets {literPerKilo} Liters per kilometer with a current cost of {fuelCost} pound(s) per liter 
would make this trip cost a total of {tripCost} pounds.''')

# $2 32kilo per (fuelCost/literPerKilo) * distance