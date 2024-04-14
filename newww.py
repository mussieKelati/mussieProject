import random

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose again.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'rock':
        return "You win! Rock crushes scissors." if computer_choice == 'scissors' else "Computer wins! Paper covers rock."
    elif user_choice == 'paper':
        return "You win! Paper covers rock." if computer_choice == 'rock' else "Computer wins! Scissors cut paper."
    elif user_choice == 'scissors':
        return "You win! Scissors cut paper." if computer_choice == 'paper' else "Computer wins! Rock crushes scissors."

def play_game():
    play_again = 'yes'
    while play_again.lower() == 'yes':
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)
        print(determine_winner(user_choice, computer_choice))
        play_again = input("Do you want to play again? (yes/no): ")

play_game()
