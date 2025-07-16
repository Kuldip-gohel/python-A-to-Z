# Attributes
'''
Attributes are variables associated with a class or objects of a class.

There are 2 types:
instance Attribute
class Attribute
'''

# Instance Attributes
'''
Attributes defined using self inside the __init__() or any method.
'''

# Example
class student:
    def __init__(self,name,roll_no):
        self.name = name  # instance attribute
        self.roll_no = roll_no

s1 = student("nilesh",26)
s2 = student("ramesh",24)

print(s1.name)
print(s2.name)

# Class Attributes
'''
Defined outside of any method, directly inside the class.
'''

# Example
class student:
    school = "GTU" #class attribute

    def __init__(self,name):
        self.name = name #instance attribute

s1 = student("mahesh")
print(s1.name)
print(s1.school)

# We also can modify the class attribute,

student.school = "python Academy"
print(s1.school) # Change class attribute for all instances

s1.school = "My school" # Overrides only for s1

# Practice Questions

# Create a Car class with instance attributes: brand, model, and a class attribute wheels = 4.
class car:
    wheels = 4

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

c1 = car("Toyota","Fortuner")
print(c1.brand)
print(c1.wheels)

# Change a class attribute value using the class name.
car.wheels = 2
print(c1.wheels)

# Add a method that prints both instance and class attributes.
class student:
    school = "JB"

    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Name is {self.name}")
        print(f"roll_no is {self.roll_no}")
        print(f"school is {self.school}")

s1 = student("mohit",23)
s1.display()
        