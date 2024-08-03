# Fahrenheit to Celsius:
# ----------------------
# Write the necessary code to convert a degree in Fahrenheit
# to Celsius and print it to the console. Use variable names!

currentTempFahrenheit = None

currentTempFahrenheit = input("What's the current temperature? (Fahrenheit)")
tempInCelsius = (int(currentTempFahrenheit) - 32) * (5/9)

print("Your current temperature in Celsus is ",tempInCelsius)