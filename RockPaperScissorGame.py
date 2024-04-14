import random

print("***Rock paper and scissors***")
print("***Let the game begin ****")
print("***Human Vs Computer****")
while True:
 human = input("Enter your choice from rock, paper, or scissors: ")
 choice_comp = ['rock', 'paper', 'scissor']
 computer = random.choice(choice_comp)
 if human == "paper":
      if computer == "rock":
          print("you win")
      elif computer == "scissor":
          print("computer wins")
      elif computer == "paper":
          print("try again")
      elif computer == "paper":
          print("try again")
 elif human == "rock":
        if computer == "rock":
            print("try again")
        elif computer == "paper":
            print("computer wins")
        elif computer == "scissor":
            print("you win")
 elif human == "scissor":
        if computer == "scissor":
            print("try again")
        elif computer == "paper":
            print("you win")
        elif computer == "rock":
            print("computer wins")



