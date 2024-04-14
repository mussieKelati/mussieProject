# first calculator
print("choose from the menu")
print("Choose 1 for addtion")
print("Choose 2 for subtraction")
print("Choose 3 for divison")
print("Choose 4 for multiplication")
choose = int(input("choose the opretor   "))
if choose == 1:
    num1 = int(input("choose the first number"))
    num2 = int(input("choose the second number"))
    total = num1 + num2
    print(total)
elif choose == 1:
    num1 = int(input("choose the first number: "))
    num2 = int(input("choose the second number: "))
    total = num1 + num2
    print(total)
elif choose == 2:
    num1 = int(input("choose the first number: "))
    num2 = int(input("choose the second number:"))
    total = num1 - num2
    print(total)
elif choose == 3:
    num1 = int(input("choose the first number:"))
    num2 = int(input("choose the second number"))
    total = num1 / num2
    print(total)
elif choose == 4:
    num1 = int(input("choose the first number"))
    num2 = int(input("choose the second number"))
    total = num1 * num2
    print(total)
else:
    print("choose from 1-4 ")