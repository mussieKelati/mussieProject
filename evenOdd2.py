class evenodd:
    def __init__(self,num):

     while True:
        num = int(input("give the number"))

        if num % 2 == 0:
            print("its even")
        else:
            print("its odd")



evenodd1 = evenodd(2)
