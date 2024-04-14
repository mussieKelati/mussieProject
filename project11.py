def length_conversion(value, source_unit, target_unit):
    if source_unit == "m":
        if target_unit == "cm":
            return value * 100
        elif target_unit == "km":
            return value / 1000
    elif source_unit == "cm":
        if target_unit == "m":
            return value / 100
    elif source_unit == "km":
        if target_unit == "m":
            return value * 1000
    # return value

def weight_conversion (value,source_unit,target_unit):
    if source_unit == "kg":
        if target_unit == "g":
             return  value * 1000
        elif target_unit == "lb":
            return  value *2.20462
    elif source_unit == "g":
        if target_unit == "kg":
            return  value /1000
        elif target_unit == "lb":
            return  value *0.00220462
    # return  value

def temprature_conversion(value,source_unit, target_unit):
    if source_unit == "C":
        if target_unit == "F":
            return  (value*9/5)+32
    elif source_unit == "F":
        if target_unit == "C":
            return (value-32)*5/9
    # return value



def mainInput():
 while True:

    print("welcome to converter")
    print("write for length 1 ")
    print("write for temperature 2 ")
    print("write for weight 3 ")

    unitchanger = int(input("choose from the above numbers"))
    source_unit = input("enter the source unit")
    target_unit = input("enter the target unit")
    value = float(input("enter the value number"))
    if unitchanger == 1:
        result = length_conversion(value,source_unit,target_unit)
        print(result)
    elif unitchanger == 2:
        result =temprature_conversion(value, source_unit, target_unit)
        print(result)
    elif unitchanger == 3 :
        result = weight_conversion(value,source_unit, target_unit)
        print(result)
mainInput()
