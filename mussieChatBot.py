def chat_bot():
    chat_chat = {"greeting": "hello how are u","todays lesson": "we are learning python",
                    "defult":"am not familar with it ", "bye": "good bye ",
                 "how was the weather today": "its good" ,"where are you":
                       "am at kabalagala train up"





                 }


    while True:
        user_input = input("user:").lower()
        if user_input in chat_chat:
            print("chatbot: ", chat_chat[user_input])
        elif user_input == "exit":
            print("chatbot: ",chat_chat["bye"])
            break
        else:
            print("chatbot: ",chat_chat["defult"])


chat_bot()