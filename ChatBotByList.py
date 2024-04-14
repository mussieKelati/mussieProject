def chatt_bot():
   while True:
    greeting = ["hi", "hello","how are u"]
    computer = "am good how are you"
    user_input = input("user: ")
    if user_input in greeting:
        print(computer[0:])


chatt_bot()