
correctPass = "12345"

gInput = input("Guess the password: ")


while gInput != correctPass:
    print("Incorrect password. pls Try again.")
    gInput = input("Guess the password: ")

print("Congratulations! Welcome to the program")
