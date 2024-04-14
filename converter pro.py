print("welcome to converter")
print("write for length 1 ")
print("write for temperature 2 ")
print("write for weight 3 ")
while True:
    
    typeconverter = int(input("choose the type of conversion:  "))
    if typeconverter == 1:
     print("for m to cm  write 1")
     print("for cm to m  write 2 ")
     print("for m to km  write 3")
     print("for km to m  write 4")
     typeUnit = int(input("choose the type of unit "))
     if   typeUnit == 1:
         mmeter = int(input("Enter the number "))
         result = mmeter *  100
         print(result)
     elif typeUnit == 2:
         centimeter = int(input("enter the number"))
         centimeter/= 100
         print(centimeter)
     elif typeUnit == 3:
         meter = int(input("enter the number"))
         meter /= 1000
         print(meter)
     elif typeUnit == 4:
         kilometer = int(input("enter the number"))
         kilometer *= 1000
         print(kilometer)
    elif  typeconverter == 2:

        print("for c to f  write 1")
        print("for f to c  write 2 ")
        typeUnit = int(input("choose the type of unit "))
        if typeUnit == 1:
         c = int(input("enter the number"))
         f = (c*9/5)+32
         print(f)
        elif typeUnit == 2:
         f = int (input("enter the number"))
         c = (f-32)*5/9
         print(c)
    elif typeconverter == 3:
        print("for kg to g write 1 ")
        print("for g to kg  write 2")
        print("for kg to lb (pounds) write 3")
        print("for lb to kg  write 4")
        typeUnit = int(input("choose the type of unit "))
        if typeUnit == 1:
            g = int(input("enter the number"))
            kg= g*1000
            print(kg)
        elif typeUnit == 2:
            kg = int(input("enter the number"))
            g = kg/1000
            print(g)
        elif typeUnit == 3:
            lb = int(input("ENTER THE NUMBER"))
            kg = lb * 2.20462
            print(kg)
        elif typeUnit == 4:
            kg = int(input("enter the number"))
            lb =  kg /2.20462
            print(lb)
    else:
     print("error")











