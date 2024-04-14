import random

print("this is guessing game")
print("please try and guess the number that is I am thingking off")
number = random.randint(1,10)
while True:
     usernum = int(input("enter the number"))
     if usernum > number:
         print("the number that u hv is to high")
     elif usernum < number:
         print("the number u hv is given is too low")
     elif usernum == number:
         print(("you win"))
