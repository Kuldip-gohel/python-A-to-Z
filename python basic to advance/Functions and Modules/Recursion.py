# Recursion
'''
Recursion is a process in which a function calls itself directly or indirectly to solve a problem.

Every recursive function must have a base case (stopping condition).
'''

# syntax:
'''
def function_name(parameter):
    if base_condition:
        return base_value
    else:
        return function_name(smaller_input)
'''

#  Example 1: Factorial Using Recursion
def factorial(n):
    if n==0 or n==1:
        return 1 #Base case
    else:
        return n*factorial(n-1) # recursive call

print(factorial(5))

# Example 2: Fibonacci Sequence Using Recursion
def fibonaki(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonaki(n - 1) + fibonaki(n - 2)
    
print(fibonaki(10))

# Example 3: Sum of Natural Numbers
def sum(n):
    if n==1:
        return 1
    else:
        return n + sum(n - 1)
    
print(sum(5))

