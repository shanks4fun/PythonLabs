# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.


name = input("What is your name? ")

blankPosition = name.find(" ")

if blankPosition == -1:
    print(f"Greeting and salutations {name}!  It's a pleasure to have you with us.")
else:
    firstName = name[:blankPosition]
    print(f"Greeting and salutations {firstName}!  It's a pleasure to have you with us.")
