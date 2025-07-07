# Function Argument
'''
- Arguments are values passed into a function when it's called.
- You can pass any number of arguments to a function.
'''

# Types of Function Arguments
'''
| Type                | Description                                                                  |
| ------------------- | ---------------------------------------------------------------------------- |
|   Positional        | Passed in order (left to right).                                             |
|   Keyword           | Passed with key=value format.                                                |
|   Default           | Has a default value if not provided.                                         |
|   Variable-length   | Accepts many values using  *arg   (positional) or  **kwarg   (keyword args). |
'''

# Return Value
'''
- A function can return a value using the return keyword.
- The returned value can be stored in a variable or used directly.
'''
# Examples of Function Arguments & Return Values

# 1. Positional Arguments
def intro(name, age):
    print(f"Your name is {name} and you are {age} years old.")

intro("kuldip",20)

# 2. Keyword Arguments
intro(name="kuldip",age=20) #order doesnot matter

# 3. Default Arguments
def num(n=1):
    print(f"this is default -> {n}")

num()
num(5) #Hear, value was changed

# 4. Variable-length Arguments (*args)
def add_all(*num):
    return sum(num)

print(add_all(1,2,3,4,5))

# 5. Return Values
def square(x):
    return x*x

res = square(5)
print(res)


# Practice Questions

# Write a function that takes two numbers and returns their average.
def avg():
    n1 = int(input("Enter 1st number -->"))
    n2 = int(input("Enter 2nd number -->"))
    return (n1+n2)/2

result = avg()
print(result)

# Write a function that takes a string and returns its reverse.
def rev():
    str = input("Enter a string -->")
    return str[::-1]

reverse = rev()
print(reverse)

# Write a function with default argument country="India" and prints it.
def country(con="India"):
    print(f"You live in {con}")

country()

# Write a function that takes any number of values using *args and returns their product.
def product(*args):
    result = 1
    for i in args:
        result *= i
    return result

print(product(2,3,4))

# Write a function that returns both the maximum and minimum from a list.
def min_max(list):
    return min(list),max(list) 

print(min_max([4,5,6]))

# Write a function that takes a list of numbers and returns only the even numbers.
def even_no(num):
    even = []
    for i in num:
        if (i%2==0):
            even.append(i)
    return even

print(even_no([1,2,3,4,5,6,7,8,9]))

# Create a function that takes age as a parameter and returns if the person is a minor or adult.
def check(age):
    if age>17:
        return "adult"
    else:
        return "minor"

print(check(17))

# Write a function that accepts a sentence and returns the number of words.
def count(word):
    sentence = word.split() 
    return len(sentence)

print(count("python is batter language"))