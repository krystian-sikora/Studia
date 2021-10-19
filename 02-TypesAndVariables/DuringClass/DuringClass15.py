# During class
# 15. Write a program that reads the temperature in degrees Celsius
# from the keyboard. The program then calculates and displays
# the temperature in Kelvin and Fahrenheit.

tempincelsius = int(input("Enter temperature in Celsius: "))
tempinkelvins = 273.15 + tempincelsius
tempinfahrenheits = 1.8 * tempincelsius + 32

print(f"Kelvins: {tempinkelvins}\nFahrenheits: {tempinfahrenheits}")