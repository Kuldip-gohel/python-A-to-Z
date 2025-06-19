'''
A while loop is used to repeat a block of code as long as a condition is True.
It's useful when you don’t know in advance how many times you need to loop — the condition controls the repetition.
'''

#Syntax
'''
while condition:
    #code block

The loop continues until the condition becomes False
'''

# Example
i = 1
while i<=5:
    print(i)
    i += 1

# Example 
n = 5
while n > 0:
    print(n)
    n -= 1

# Some Practice Question.

# Print numbers from 1 to 10 using a while loop.
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1

# Print even numbers from 2 to 20.
i = 2
while i <= 20:
    if (i%2==0):
        print(i, end=" ")
    i += 1

# Ask the user to enter a password until they enter the correct one.
password = "kuldip1234"

while True:
    enter_pass = input("Enter password -->")

    if enter_pass==password:
        print("Access Granted")
        break
    else:
        print("Incorrect Password, Try again.")

# Find the sum of numbers from 1 to N (user input).
num = int(input("Enter Any number -->"))
i = 1
total = 0

while i <= num:
    total += i
    i += 1

print("sum is, ", total)

# Multiplication Table using while loop
number = int(input("Enter a number --> "))
i = 1
while i <= 10:
    print(f"{number} x {i} = ",number*i)
    i += 1

# Keep Asking for Numbers Until Negative is Entered
while True:
     num = int(input("Enter any number -->"))
     if num < 0:
         print("Enter positive number")
         break
     print(f"You entered {num}")
     break
    
