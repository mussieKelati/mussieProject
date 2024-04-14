import random

while True:
    human = input("person 1 : Choose from 'heads' or 'tails'  ")
    human2 = input("person 2 : Choose from 'heads' or 'tails'  ")
    computer = random.choice(['head', 'tail'])

    if human == computer:
        print("Congratulations!  person 1 win ")
    else:
        print("Congratulations!  person 2 win ")
