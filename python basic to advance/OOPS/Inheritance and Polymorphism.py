# Inheritance 
'''
Inheritance is a feature in object-oriented programming where a child class inherits methods and attributes from a parent class. It promotes code reuse.
'''

# Syntax
'''
class parent:
    # code

class child(parent):
    # child class inherits from parent
'''

# Example
class animal:
    def sound(self):
        print("Animal make sound")

class Dog(animal):
    def bark(self):
        print("woof! woof!")

d = Dog()
d.bark() # Own method
d.sound() # inherited

# Polymorphism
'''
Polymorphism means "many forms". In Python, it allows different classes to define the same method name but with different behaviors.
'''

# Example
class Bird:
    def sound(self):
        print("Tewwt")

class cat:
    def sound(self):
        print("Meow")

def make_sound(animal):
    animal.sound()

b = Bird()
c = cat()
make_sound(b)
make_sound(c)

# Practice Questions

# Create a class Person with name and age, then create a child class Student with an extra attribute: marks.
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name is {self.name}")
        print(f"age is {self.age}")

class student(person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def show_info(self):
        super().show_info()
        print(f"Marks is {self.marks}")

s = student("ramesh",18,96)
s.show_info()
        
# Create a base class Vehicle and two derived classes Car and Bike with their own methods.
class vehical:
    def __init__(self, brand):
        self.brand= brand

    def intro(self):
        print(f"Brand name is {self.brand}")

class car(vehical):
    def __init__(self, brand, car_name):
        super().__init__(brand)
        self.car_name = car_name

    def intro(self):
        super().intro()
        print(f"Car name is {self.car_name}")

class Bike(car):
    def __init__(self, brand, car_name, Bike_name):
        super().__init__(brand, car_name)
        self.Bike_name = Bike_name

    def intro(self):
        super().intro()
        print(f"bike name is {self.Bike_name}")

B = Bike("BMW","2 Series","S 1000 RR")
B.intro()

# Write a program where a child class overrides a method from the parent class.
class parent:
    def avg(self,total,count):
        print(f"Avg is {total/count}")

class child(parent):
    def sum(self,a ,b):
        print(f"Sum is {a+b}")

c = child()
c.sum(5,10)
c.avg(1000,3)

# Create two classes Circle and Square both with a method area(). Use polymorphism to call them.
class circle:
    def __init__(self,r):
        self.r = r

    def area(self):
        print(f"Area of circle is {3.14*(self.r**2)}")

class square:
    def __init__(self,l,w):
        self.l = l
        self.w = w

    def area(self):
        print(f"Area of square is {self.l*self.w}")

def count_area(Area):
    Area.area()

c = circle(8)
s = square(4,5)
count_area(c)
count_area(s)

# Implement a method describe() in multiple classes (like Employee, Manager, Intern) with different behaviors.

class employee:
    def describe(self):
        print("It is an employee")

class manager:
    def describe(self):
        print("It is a manager")

class Intern:
    def describe(self):
        print("It is an intern")
        
def describe(des):
    des.describe()

e = employee()
m = manager()
i = Intern()
describe(e)
describe(m)
describe(i)

# Use a loop to call the same method from different class objects stored in a list.

class dog:
    def sound(self):
        print(f"Dog is bark.")

class cat:
    def sound(self):
        print(f"cat is meaw.")

class cow:
    def sound(self):
        print("cow is moo.")

animals=[dog(),cat(),cow()]

for i in animals:
    i.sound()