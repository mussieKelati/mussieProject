class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob


person1 = Person("abel kibreab", "Eritrea", "1997-05-15")
print("Name:", person1.name)
print("Country:", person1.country)
print("Date of Birth:", person1.dob)
