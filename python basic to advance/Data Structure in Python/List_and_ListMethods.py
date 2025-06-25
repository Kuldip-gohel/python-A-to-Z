# List
'''
A list is a collection of items that is ordered, changeable (mutable), and allows duplicate elements.
Lists can store any data type: strings, numbers, or even other lists.
'''

# How to create a List:
fruits = ["Apple","Banana","Orange","Mango"]
number = [1,2,3,4,5]
mix = ["hello",5.45,6,"good morning",True]
print(mix) #['hello', 5.45, 6, 'good morning', True]

# Accessing List Elements
print(fruits[0]) #Apple
print(fruits[-1]) #Mango
print(mix[1:5]) #[5.45, 6, 'good morning', True]


# Common List Methods 
# append()          = Add item at the end
# insert(index, x)	= Add item at specific index
# remove(x)	        = Remove first occurrence of value	
# pop()	            = Remove and return last item	
# pop(index)	    = Remove item at specific index	
# sort()	        = Sort list in ascending order	
# reverse()         = Reverse the order of the list	
# count(x)       	= Count how many times x appears	
# index(x)          = Get index of first occurrence of x	
# clear()	        = Remove all items from list	
# copy()	        = Create a copy of the list	


# Some Examples
num = [1, 2, 3]
num.append(4)
print(num) #[1, 2, 3, 4]

num.insert(1,0.5) #in 1st index, insert 0.5
print(num) #[1, 0.5, 2, 3, 4]

num.remove(0.5)
print(num) #[1, 2, 3, 4]

num.pop() #Last item was poped
print(num) #[1, 2, 3]

num.reverse()
print(num) #[3, 2, 1]
 

# Practice Questions 

# Create a list of your 5 favorite movies and print it.
Movies = ["Jhon Wick","Avengers Endgame","Faatine","Spider-Man","Venom"]
print(Movies)

# Add a new item to a list using .append() and .insert().
Movies.append("RRR")
Movies.insert(2,"Devra")
print(Movies)

# Remove a specific item from a list using .remove() and .pop().
Number = [1,2,3,5,8]
Number.remove(5)
Number.pop()
print(Number)

# Sort a list of numbers and then reverse it.
list = [1,5,9,4,7,6,3,2,8]
list.sort()
print(list)
list.reverse()
print(list)

# Count how many times a value appears in a list.
num = [1,2,6,9,6,4,6,7,6]
print(num.count(6))

# Find the largest and smallest number in a list.
li = [40,80,44,60,20,90]
large = max(li)
small = min(li)
print(large)
print(small)
    
# Take 5 numbers from user input and store them in a list.
num = []
for i in range(5):
   number = int(input(f"Enter number -->"))
   num.append(number)

print(num)

# Make a list of even numbers between 1 to 20.
even = []
for i in range(1,21):
    if i%2==0:
        even.append(i)

print(even)

# Copy a list and clear the original one.
name = ["Mohan","Rphan","sohan"]
new = name.copy()
print(new)
name.clear()
print(name)

# Loop through a list and print only the items that start with a vowel.
list = ["Apple","Mango","Orange","Graps"]
vowel = "aeiouAEIOU"
for i in list:
    if i and i[0] in vowel:
        print(i)

