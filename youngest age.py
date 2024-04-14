age1 = int(input("Enter age of person 1: "))
age2 = int(input("Enter age of person 2: "))
age3 = int(input("Enter age of person 3: "))
age4 = int(input("Enter age of person 4: "))
youngest_age = age1

if age2 < youngest_age:
    youngest_age = age2
if age3 < youngest_age:
    youngest_age = age3
if age4 < youngest_age:
    youngest_age = age4

print((youngest_age) )

