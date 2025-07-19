# Method Overriding
'''
Method Overriding occurs when a child class provides its own implementation of a method that is already defined in the parent class.

It is a key concept of polymorphism in object-oriented programming.
'''

# Example
class animal:
    def speak(self):
        return "some sound"
    
class dog(animal):
    def speak(self):
        return "bark"

class cat(animal):
    def speak(self):
        return "Meow"

D = dog()
C = cat()
print(D.speak())
print(C.speak())

# Operator Overloading
'''
Operator Overloading allows us to define how built-in operators like +, -, *, etc. behave for user-defined classes.
'''

# Example
class point:
    def __init__(self,x,y):
        self.x = x 
        self.y = y
        
    def __add__(self,other):
        return point(self.x + other.x,  self.y + other.y)
    
    def __str__(self):
        return f"{self.x},{self.y}"
    
p1 = point(1,2)
p2 = point(3,4)

result = p1 + p2
print(result)

# Practice Questions

# Create a base class Shape with a method area(). Override this method in subclasses Rectangle and Circle.
class shape:
    def area(self):
        return "Area is not define."

class rectangle(shape):
    def __init__(self,w,l):
        self.l = l
        self.w = w

    def area(self):
        return f"Area of rectangle is {self.l*self.w}"
    
class circle(shape):
    def __init__(self,r):
        self.r = r

    def area(self):
        return f"Area of circle is {3.14*(self.r**2)}"
        
R = rectangle(4,5)
c = circle(3)
print(R.area())
print(c.area())

# Define a class Person with a method greet(). Override it in classes Teacher and Student with different messages.
class person:
    def greet(self):
        return "This is a person."

class Teacher(person):
    def greet(self):
        return "This is a teacher."

class student(person):
    def greet(self):
        return "this is a student."

T = Teacher()
S = student()
print(T.greet())
print(S.greet())

# Create a class Time with hours and minutes. Overload the + operator to add two time objects.
class time:
    def __init__(self,minutes,houres):
        self.minutes = minutes
        self.houres = houres
        
    def __add__(self,other):
        total_minutes = self.minutes + other.minutes
        total_houres = self.houres + other.houres + (total_minutes // 60)
        total_minutes = total_minutes % 60
        return time(total_houres, total_minutes)

    def display(self):
        print(f"{self.houres} hours and {self.minutes} mins")

t1 = time(2,50)
t2 = time(1, 30)
t3 = t1 + t2
t3.display()

# Make a class Book with a price attribute and overload the > operator to compare prices.
class Book:
    def __init__(self, price):
        self.price = price

    def __gt__(self, other):
        return self.price > other.price

# Example
book1 = Book(450)
book2 = Book(300)

if book1 > book2:
    print("Book 1 is more expensive")
else:
    print("Book 2 is more expensive")

