# Lambda Function
'''
A lambda function is a small, anonymous function in Python.
It is used when you need a short function for a short period of time.
'''

# Syntax:
'''
lambda arguments: expression

- Can have any number of arguments
- Contains only one expression (no loops, no multiple lines)
'''

# Examples
add = lambda a, b:a + b
print(add(3,2))

square = lambda a: a*a
print(square(5))

# Lambda with map(): Square Each Number in a List
number = [1,2,3,4,5]
square = list(map(lambda x:x*x,number))
print(square)

# Lambda with filter(): Filter Even Numbers
number = [1,2,3,4,5,6,7,8,9]
even = list(filter(lambda x:x%2 == 0,number))
print(even)


# Practice Questions

# Write a lambda to multiply two numbers.
multiply = lambda a, b: a*b
print(multiply(45,63))

# Use lambda with map() to cube each number in a list.
num = [1,2,3,4,5]
cube = list(map(lambda a:a*a*a,num))
print(cube)

# Use lambda with filter() to find numbers greater than 10.
num = [12,15,9,6,5,10,18,45,2]
grater = list(filter(lambda x:x>10, num))
print(grater)

# Use a lambda in a max() function to find the tuple with the largest second value.
pairs = [(1, 3), (2, 5), (4, 1), (7, 9)]
larjest = tuple(max(pairs,key=lambda x:x[1]))
print(larjest)

# Create a lambda that returns True if a string starts with a vowel.
vowel = lambda a:a[0].lower() in "aeiou"
print(vowel("Apple"))
print(vowel("mango"))

# Write a lambda that returns the last character of a string
last_char = lambda x:x[-1]
print(last_char("python is easy language"))

# Combine lambda and map() to add 5 to every number in a list.
li = [1,2,3,4,5]
add = list(map(lambda a:a+5,li))
print(add)