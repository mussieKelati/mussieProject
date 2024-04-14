
number = int(input("Enter a number: "))
factorial = 1
current_number = 1
while current_number <= number:         # current = 1     number = 10
    factorial = current_number * factorial                  # factorial = 1   current number = 1     f = 1
    current_number += 1

print(factorial)
