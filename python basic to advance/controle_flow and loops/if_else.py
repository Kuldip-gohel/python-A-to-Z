# if_else :-
''' The if-else statement is used to make decisions in your program.
 It allows your code to take different paths based on conditions.
 '''

# Syntax:
'''
if condition:
    # code block if condition is True
else:
    # code block if condition is False
'''
# you can also use elif (else if) to check multiple conditions:
'''
if condition1:
      # condition according your need
elif condition2:
      # another condition 
else:
      # if no one condition is satisfy  then execute this block
'''

# Example
age = int(input("Enter Your age -->"))

if age < 12:
    print("You are a child")
elif age >= 12 and age < 18:
    print("You are adolescence")
else:
    print("You are adult")

# Another practice examples

# Take a number from the user and check if it’s even or odd.
num = int(input("Enter any number -->"))
if (num%2==0):
    print(f"Number {num} is Even")
else:
    print(f"number {num} is Odd")

# Ask for marks and print grade using if-elif-else.
marks1 = int(input("Enter Maths marks -->"))
marks2 = int(input("Enter science marks -->"))
marks3 = int(input("Enter phycology marks -->"))
Average = (marks1 + marks2 + marks3)/3

if (Average>90):
    print(f"Your Grade is \'A\'")
elif (Average <= 90 and Average > 75):
    print(f"Your Grade is \'B\'")
elif (Average <=75  and Average >= 50):
    print(f"Your Grade is \'C\'")
else:
    print(f"Your Grade is \'D\'")


# 3.Create a basic login system that checks if username is correct.
login = input("Enter username -->")
username = "Kuldip@gmail.com"

if (login == username):
    print(f"username {login} is Veryfied")
else:
    print("Enter a valid username")

# 4. Check if a number is positive, negative, or zer
number = int(input("Enter any number -->"))
if (number > 0):
    print("Enterd number is positive")
elif (number == 0):
    print("Enterd number is 0")
elif (number < 0):
    print("Enterd number is Negative")
else:
    print("Enter a valid number(Value)")

# 5. Compare two numbers and print the larger one.
n1 = int(input("Enter First number -->"))
n2 = int(input("Enter Second number -->"))

if (n1 > n2):
    print(f"number {n1} is larger")
else:
    print(f"number {n2} is larger")