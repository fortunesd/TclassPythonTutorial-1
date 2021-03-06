# A class is a blueprint for creating objects. A object has properties and methods(functions) associated with it
# Almost everything in Python is an object that is why Python is an object oriented programming language- OOP

# Create class

class Students:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'I am a student with name {self.name} and i am {self.age}'

    def has_birthday(self):
        self.age += 1



# Extend class (inheritance)

class StudentRep(Students):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'I am the class rep with name {self.name} and i am {self.age} and my balance is {self.balance}'

    
# Create an Object of class Students
fortune = Students('Onyekwere Fortune', 'onyekwerfortune1@gmail', 21)

# Create an Object of class StudentRep
joshua = StudentRep('Ndubueze Joshua', 'josheze58@gmailcom', 20)

joshua.set_balance(800)
print(joshua.greeting())