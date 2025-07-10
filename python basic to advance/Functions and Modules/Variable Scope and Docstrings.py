#  Variable Scope
'''
Variable scope defines where a variable can be accessed or modified in your program.

There are mainly four types of scopes in Python:

| Scope Type    | Description                                             |
| ------------- | ------------------------------------------------------- |
|   Local       | Inside a function, only accessible within that function |
|   Global      | Declared outside all functions, accessible everywhere   |
|   Enclosing   | For nested functions, outer function’s scope            |
|   Built-in    | Names pre-defined by Python (e.g., print,len)           |

'''

# Examples:
x = 10 #Globle variable

def fun():
    x = 5 #Local variable
    print("Inside function ",x)

fun()
print("outside function",x)

# Practice Questions

# Write a function that modifies a global variable using global.
a = 10

def modify_globle():
    global a
    a += 1

modify_globle()
print(a)

# Try to print a local variable outside the function — observe what happens

def try_to_print():
    k = 10
    print(k)

try_to_print()
# print(k) # it will throw error like,  name 'k' is not defined

# Docstrings
'''
A docstring is a special string used to document what a function, class, or module does.
It helps users understand your code.

- Placed inside triple quotes """
- Comes just after the function or class definition
'''

# Example

def intro(name):
    """
    This function takes a name.
    """
    print(name)

intro("Raman")

# You can access the docstring using:
print(intro.__doc__)

# Multi-line Docstring Example
def add(a,b):
    """
    Add two numbers.

    parameter:
    a -- first number
    b -- second number

    returns: 
    sum of a and b
    """
    return a + b

print(add(4,5))

