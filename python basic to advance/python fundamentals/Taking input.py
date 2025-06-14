'''The input() Function is used to taking input from the user.
It always returns the input as a string,
so you may need to convert it using type casting (int(), float(), etc.) if needed.
'''

#For Example
input("Enter somthing -->") #just take input not print it.

name = input("Enter Your name -->") #taking input
print(name) #print name taken by input() function

Age = int(input("Enter your age -->")) #take as int value
print(Age) 
print(f"Hello your name is {name} and you are {Age} years old") #This is f' string use like that

# Examples

# Take two numbers from the user, add them, and print the result.
a = int(input("Enter first number -->"))
b = int(input("Enter second number -->"))
result = a + b
print("Addition is -->",result)

#Ask the user for a float number and print its square.
k = float(input("Enter a floating number -->"))
squre = k*k
print("squre of float number is -->",squre)

# Ask the user if they are a student (yes/no), and print a message based on it.
student = input("Are you a student (yes/no)-->")
print(student)