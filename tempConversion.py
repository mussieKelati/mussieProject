# while True:
#     c = float(input("Enter the Celsius temperature: "))
#     for temp in range(1):
#         fahrenheit = (c * 9/5) + 32
#

from_celsius = float(input("Enter the start Celsius temperature: "))
to_celsius = float(input("Enter the end Celsius temperature: "))
for celsius in range(int(from_celsius), int(to_celsius)):
    fahrenheit = (celsius * 9/5) + 32
    print(str(celsius) , str(fahrenheit))

