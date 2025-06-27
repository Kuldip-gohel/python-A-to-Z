# Set
'''
A set is a built-in Python data type that is:
- Unordered (no indexing)
- Unchangeable (immutable) elements but mutable set
- Does not allow duplicates

Sets are useful when you want to store unique values or perform set operations like union, intersection, etc.
'''

# Creating a Set
fruits = {"Apple","orange","banana"}
num = {1,2,3,4}
mix = {"Hello",25,True,5.5}
print(mix)

# Empty Set (Use set(), not {})
empty_set = set()
print(type(empty_set)) #<class 'set'

# Examples
my_set = {1,2,3,3,5,6,9,5}
print(my_set) #{1, 2, 3, 5, 6, 9}, remove duplicates

# Common Set Methods
'''
add(x) = Add element x to the set
update([x, y]) = Add multiple elements
remove(x) = Remove x (raises error if not found)
discard(x) = Remove x (doesn't raise error)
pop() = Removes random element
clear() = Removes all elements
copy() = Returns a copy
'''

#  Set Operations
'''
Union = |
Intersection = & or set1.intersection(set2)
Difference =   - or set1.difference(set2)
Symmetric Diff. =  ^ or set1.symmetric_difference(set2)
'''

# Example:
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b) # union -> {1, 2, 3, 4, 5}
print(a & b) # Intersection -> {3}
print(a - b) # Difference -> {1, 2}
print(a ^ b) # Symmetric Diff. -> {1, 2, 4, 5}

# Practice Questions

# Create a set of 5 fruits and add one more fruit.
fruits = {"Apple","Banana","Graps","Orange","Mango"}
fruits.add("Watermelon")
print(fruits) 
 
# Add multiple numbers to a set using update().
x = {1,2,3,4,5}
x.update([6,7,8,9])
print(x) 

# Remove a specific item using discard() and remove(). Try removing a non-existing one.
fruits = {"Apple","Banana","Graps","Orange","Mango"}
fruits.discard("Mango") 
print(fruits)
fruits.remove("Apple")
print(fruits)
# fruits.remove("Watermalon")
# print(fruits) # If Value not found then it throw an error
fruits.discard("watermalon") 
print(fruits) # If Value not found then it will not throw an error

# Take input of 5 numbers from the user and store only unique numbers in a set.
unique = set()
for i in range(5):
    n = int(input(f"Enter num {i + 1} --> "))
    unique.add(n)
print("Unique values you entered:", unique)
  
# Find the union and intersection of two sets.
a = {1,2,3}
b = {5,6,3}
print(a.union(b))
print(a.intersection(b))

# Create two sets of programming languages and find:
# - Only in first set
# - Common to both
# - Present in either but not both
set1 = {"Python","Javascript","c","c++"}
set2 = {"Python","Django","Flask","MongoDb"}
print(set1 - set2)
print(set1 & set2)
print(set1 ^ set2)

# Count the number of unique letters in a word.
word = input("Enter Word -->")
stor = set(word)
print(len(stor))

# Convert a list with duplicates to a set.
list = ["red","green","red","yellow","blue","orange"]
convert = set(list)
print("set with unique colors -->",convert)
print("original list -->",list)

# Create a copy of a set and clear the original.
set = {"red","blue","green","yellow","purple"}
copy = set.copy()
print(copy)
set.clear()
print(set)

# Check if one set is a subset or superset of another.
set1 = {1,2,3,4,5}
set2 = {1,2}
print(set1.issubset(set2))
print(set1.issuperset(set2))



