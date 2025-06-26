# Tuple
'''
A tuple is a collection of items, like a list, but it is immutable, meaning you can't change, add, or remove elements after it's created.
- Tuples are defined using round brackets ().
- Useful for storing fixed data, e.g., days of the week, coordinates, etc.
'''

# Example
fruits =  ("Apple","Orange","Banana")
mix = ("mohan",21,True)
single_item = ("hello", ) # comma is neccesary without comma it will become a string.
colors = "red","green","orange" # Tuple without parentheses (optional, but not recommended)
print(single_item)

# Accessing Tuple Elements
print(fruits[0]) #Apple
print(fruits[-1]) #Banana

# Tuple is Immutable
fruits = ("apple", "banana")
# fruits[0] = "mango"   # It will throw error,  Error: 'tuple' object does not support item assignment


'''
Common Tuple Methods

count(x) = Returns how many times x appears
index(x) = Returns the first index of x
'''

# Tuple Functions
t = (1,2,3,4)
print(max(t))
print(min(t))
print(len(t))
print(sum(t))

# Practice Questions

# Create a tuple with 5 numbers and find their sum.
tup = (1,2,3,4,5)
print(sum(tup))

# Make a tuple of your 3 favorite colors and print each using a loop.
colors = ("Orange","black","Blue")
for i in colors:
    print(i)

# Create a tuple of even numbers from 1 to 10.
even = tuple()

for i in range(1, 11):
    if i % 2 == 0:
        even += (i,)

print("Tuple of even numbers from 1 to 10:", even)


# Check whether a value exists in a tuple (use in keyword).
user = input("Enter any vegitable -->")
veg = ("onion","photato","lamon")
if user in veg:
    print("Veg.. available")
else:
    print("Veg.. is not available")

# Find the index of a specific value in a tuple.
tup = (1,2,3,4,5)
print(tup.index(2))

# Count how many times a word appears in a tuple.
number = (1,2,3,54,4,5,7,4,10,4,9,4,11)
print(number.count(4))

# Convert a list to a tuple using tuple() and print it.
list = ["Apple","Banana","Mango"]
tup = tuple(list)
print(tup)

# Try modifying a tuple and observe the error.
# tup = (1,2,3,4,5)
# tup[0] = 2

# Join two tuples into one and print the result.
t1 = (1,2,3)
t2 = (3,4,5)
join = t1 + t2
print(join)

# Create a tuple of city names and print the cities that start with "A".
city = ("surat","Arjentina","vadodra","mumbai","rajkot","Ahamdabad")
for i in city:
    if i.startswith("A"):
        print(i)
    
