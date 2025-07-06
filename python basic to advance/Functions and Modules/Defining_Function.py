# Function in Python
'''
A function is a reusable block of code that performs a specific task.
You can call the function whenever you want to execute that task.
'''

# How to Define a Function
'''
def function_name(parameters):
    # Code block
    return result # optional
'''

# Example
def hello():
    print("Hello World!!")

hello() #Hello World!!

# Function with Parameters
def add(a, b):
    return a + b

result = add(5,10)
print(result) #15

# Function with Default Parameters
def intro(name="mohan"):
    print(f"hello {name}")

intro() #hello mohan
intro("soham") #hello soham , we can also change default value by providing value in function calling time

# Function with Return
def square(num):
    return num * num

print(square(5)) #25


# Practice Questions

# Write a function that checks if a number is even or odd.
def even_odd():
    num = int(input("Enter any number -->"))
    if num%2==0:
        print(f"{num}, is EVEN number")
    else:
        print(f"{num}, is ODD number")

even_odd()

# Write a function that takes two numbers and returns the larger one.
def larger(a , b):
    if a>b:
        return a
    else:
        return b

print(larger(15,10))

# Write a function to calculate the factorial of a number.
def fact(num):
    result = 1
    for i in range(1,num+1):
        result *= i
    return result

print(fact(3))

# Write a function that takes a list and returns the sum of all elements.
def list_sum(n):
    total = 0
    for i in n:
        total += i
    return total

print(list_sum([1,2,3,4,5]))

# Write a function that returns True if a string is a palindrome.
def palindrom(s):
    return s == s[::-1]

print(palindrom("hello")) #False
print(palindrom("madam")) #True


# Write a function that counts vowels in a given string.
def vowels(str):
    vowel = "AEIOUaeiou"
    count = 0
    for i in str:
        if i in vowel:
           count += 1
    return count

print(vowels("hello mohan"))

# Write a function that checks whether a given year is a leap year.
def leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(leap_year(2023)) #False
print(leap_year(2024)) #True