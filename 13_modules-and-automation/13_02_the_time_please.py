# Use a built-in Python module to tell you the current date and time.
# Research online, so you can print it in a readable manner.
from datetime import datetime

now = datetime.now()

print("Current date:", now.strftime("%m-%d-%Y"))

# Print the current time in HH:MM:SS format
print("Current time:", now.strftime("%H:%M:%S"))
