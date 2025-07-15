# Constructor 
'''
A constructor is a special method that is automatically called when an object is created from a class.

In Python, the constructor method is:

__init__(self, ...)

It is used to initialize the object’s attributes.
'''

# Syntax:
class classname:
    def __init__(self,parameter):
        self.parameter = parameter

# Hear,
# __init__ is a built-in method.

# Example
class studemnt:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(f"name: {self.name},Roll: {self.roll}")
        
# Creating an object (calls constructor)
s1 = studemnt("mohan",21)
s1.display()

# Constructure types:
'''
| Type          | Description                                |
| ------------- | ------------------------------------------ |
| Default       | No parameters (other than  self )          |
| Parameterized | Accepts arguments to initialize attributes |

'''

# Practice Questions

# Create a class Car with brand and model using a constructor.
class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"car brand is {self.brand}, model is {self.model}")

c1 = car("Toyota","supra")
c1.display()

# Write a class Phone with default and parameterized constructors.
class phone:
    def __init__(self,phone_name="unknown",price=0):
        self.name = phone_name
        self.price = price

    def display(self):
        print(f"Phone name is {self.name},price is {self.price}")

# Object with default constructor (no arguments)
p1 = phone()
p1.display()

# Object with parameterized constructor
p2 = phone("samsung",120000)
p2.display()

# Make a class Calculator that takes two numbers and performs basic operations.
class calculater:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
        
    def operation(self):
        add = self.n1 + self.n2
        multiply = self.n1 * self.n2
        division = self.n1 / self.n2
        substration = self.n1 - self.n2
        print(f"Addition is --> {add}")
        print(f"multiplication is --> {multiply}")
        print(f"division is --> {division}")
        print(f"substration is --> {substration}")

c1 =calculater(10,5)
c1.operation()

