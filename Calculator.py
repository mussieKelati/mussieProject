class Calculator:
    def addtion(x,y):
        return x+y
    def maltiply(x,y): 
        return x*y
    def subtract(x,y):
        return x-y
    def division(x,y):
        return x/y

calculator1 = Calculator
print("additon",calculator1.addtion(10,5))
print("maltiply",calculator1.maltiply(10,5))
print("division",calculator1.division(10,5))
print("subtraction",calculator1.subtract(10,5))
print("addution ",calculator1.addtion(20,5))