# Class:
'''
A class is a blueprint for creating objects. It defines properties (attributes) and behaviors (methods).
'''

# Object:
'''
An object is an instance of a class
'''

# Basic Syntax:
'''
class classsname:
    def__init__(self, parameters): #constructor
    self.attribute = ValueError

    def method(self):
        # code to run
'''

# Example: Creating a Class and Object
class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name is {self.name} and age is {self.age}")

s1 = student("kuldip",20)
s1.display()
        
# key concept
'''
| Term              | Description                                      |
| ----------------- | ------------------------------------------------ |
|  __init__( )      | Constructor: runs when object is created         |
|  self             | Refers to the current object                     |
| Instance Variable | Unique for each object ( self.name ,  self.age ) |
| Method            | Function inside a class                          |
| Object            | Created from a class ( obj = ClassName(...) )    |
'''

# Practice question

# Make a Rectangle class that calculates area
class rectangle:
    def __init__(self,length, width):
        self.length = length
        self.width = width

    def area(self):
        print(f"Area of rectangle is {self.length*self.width}")

r1 = rectangle(5,9)
r1.area()
        
# Create a BankAccount class with deposit, withdraw, and check balance methods.
class bankAccount:
    def __init__(self,balance):
        self.balance = balance
        
    def check_balance(self):
        print(f"Your Balance is --> {self.balance}")

    def deposite_amount(self,deposite):
        self.balance += deposite
        print("deposite amount is -->",deposite)
        print("With deposite amount your balance is -->",self.balance)

    def withDrow(self,withdrow):
        self.balance -= withdrow
        print("Withdrown is -->",withdrow)
        print("with Withdrown amount your balance is -->",self.balance)

    def finel_amount(self):
        print(f"Your bank Balance is -->{self.balance}")
    
a1 = bankAccount(40000)
a1.check_balance()
a1.deposite_amount(10000)
a1.withDrow(5000)
a1.finel_amount()
        

# Create a class Book that stores title, author, and price. Add a display method.
class book:
    def __init__(self,Title,Author,Price):
        self.Title = Title
        self.Author = Author
        self.Price = Price
        
    def display(self):
        print(f"Book name is {self.Title}")
        print(f"Book Author is {self.Author}")
        print(f"Book Price is {self.Price}")

b1 = book("Reach dad poor dad","Robert kiyosaki",1000)
b1.display()

# Create a Temperature class that converts Celsius to Fahrenheit.
class convert:
    def __init__(self,C):
        self.C = C

    def convertor(self):
        print(f"Fahrenheit of {self.C} is --> {self.C * (9/5) + 32}")

c1 = convert(42)
c1.convertor()

# Build a class Counter that increases count on each method call.
class Counter:
    def __init__(self):
        self.count = 0

    def increases(self):
        self.count += 1
        print(self.count)

c1 = Counter()
c1.increases()
c1.increases()
c1.increases()

# Create a class Employee and store info of multiple employees in a list.
class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def display(self):
        print(f"Name is {self.name}, age is {self.age},salary is {self.salary}")

employee = []

employee.append(Employee("mohan",20,40000))
employee.append(Employee("ram",21,50000))
employee.append(Employee("shyam",19,35000))

for i in employee:
    i.display()
        