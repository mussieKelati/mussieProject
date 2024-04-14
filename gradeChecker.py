marks = int(input("input the marks"))
if marks > 90 and marks <= 100 :
    print("Your Grade is A ")
elif marks > 80 and marks <= 90:
    print("Your  grade is B")
elif marks > 60 and marks < 80:
    print("Your grade is C")
elif marks < 60 :
    print("your grade is D")
else:
        print( "input marks from 1 - 100")
