# String Formatting
''' String formatting means inserting variables or values into strings in a clean, readable way
'''

# format() Method
'''
The format() method allows you to insert variables into a string using placeholders {}.
'''
# Example
name = "naman"
age = 21
print("My name is {} and i am {} years old.".format(name,age))

# We can also use like this,..
print("{1} is learning {0}".format("python","Alice"))
print("{name} is {age} years old".format(name="bob", age=25))


# f-Strings
'''
An f-string is a string literal with an f prefix that lets you embed variables directly using {}.
'''
# Example
name = "harprit"
age = 25
print(f"My name is {name} and i am {age} Years old.")


# Practice Questions

# Take name and age as input and display using format() and f-string.
name = input("Enter Your name -->")
Age = int(input("Enter Your Age -->"))
print("Name is {} and your age is {}".format(name,age))
print(f"Name is {name} and age is {age}")

# Ask the user for two numbers and show the sum using f-string.
a= int(input("Enter a number -->"))
b= int(input("Enter another number -->"))
print(f"sum of {a} and {b} is --> {a+b}")

# Format a float number to show only 2 decimal places.
n = 2.2345132
print(f"Float no. with 2 decimal is {n:.2f}")

# Create a sentence: "You scored X out of Y" using both methods.
x = 50
y = 48
print(f"You scored {x} out of {y}")
print("You scored {} out of {}".format(x,y))

# Ask the user for their city and country and display it using .format().
city = input("Enter your city name -->")
country = input("Enter your country name -->")
print("city is {} and country is {}".format(city,country))

# Create a mini profile summary: name, age, hobby, etc., using f-strings.
name = "marry"
age = 22
hobby = "Cricket"
print(f"My name is {name} and i am {age} Years old and my hobby is {hobby}")

# Show a bill receipt: item name, quantity, price, and total using f-strings.
item_name = "car"
quantity = 25
price = 500
total = quantity * price
print(f"item = {item_name}\nQuantity = {quantity}\nprice = {price}\nTotal = {total}")

# Create a welcome message like: Hello, [Name]! You are [Age] years old. using both methods.
name = "mohit"
age = 25
print(f"Hello, {name}! you are {age} Years old.")
print("Hello, {}! you are {} Years old.".format(name,age))

# Convert Celsius to Fahrenheit and print using f-string
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F")
