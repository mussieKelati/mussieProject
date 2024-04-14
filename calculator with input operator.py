print("Choose from the menu:")
print("Choose + for addition")
print("Choose - for subtraction")
print("Choose / for division")
print("Choose * for multiplication")

choose = input("Choose the operator: ")

if choose == "+":
    num1 = int(input("Choose the first number: "))
    num2 = int(input("Choose the second number: "))
    total = num1 + num2
    print( total)
elif choose == "-":
    num1 = int(input("Choose the first number: "))
    num2 = int(input("Choose the second number: "))
    total = num1 - num2
    print( total)
elif choose == "/":
    num1 = int(input("Choose the first number: "))
    num2 = int(input("Choose the second number: "))

elif choose == "*":
    num1 = int(input("Choose the first number: "))
    num2 = int(input("Choose the second number: "))
    total = num1 * num2
    print( total)
else:
    print("Choose from standard operators.")
