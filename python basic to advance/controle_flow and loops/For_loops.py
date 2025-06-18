'''
A for loop in Python is used to iterate over a sequence (like a list, string, range, etc.).
 - It runs the block of code for each item in the sequence.
 - It is commonly used when you know in advance how many times you want to loop.
'''

# Syntax
'''
for variable in sequence:
    # Code block to execute

'''
# Examples

# 1 example
fruits = ["banana","Watermalon","Apple"]
for fruit in fruits:
    print(fruit) # It will return all fruits name 

# 2 example
for i in range(1, 11):
    print(i)  # It will return 1 to 10 number

# 3 example
str = "My name is kuldip"
for latter in str:
    print(latter, end="") # It will return all latter present in string called str

# Now solve some practice Questions

# Print all even numbers from 1 to 50.
for i in range(1,51):
    if (i%2==0):
        print(i, end=" ")

# Print the square of numbers from 1 to 10.
for i in range(1, 11):
    print(f"Squre of {i} is",i*i)

# Calculate the sum of numbers from 1 to 100 using a loop.
sum = 0
for i in range(1,101):
    sum = sum+i # we can also write 'sum += i'

print(sum)

# Print a multiplication table for a number entered by the user.
number = int(input("Enter a number -->"))
for i in range(1, 11):
    print(f"{number} x {i} =",number*i)

# Count vowels in a string entered by the user.
str = input("Enter a string i will find vowels in that string -->")
voweles = "aeiouAEIOU"
count = 0

for vowel in str:
    if vowel in voweles:
        count += 1
    
print("Number of vowels :", count)
        
# Loop through a list of names and print only names that start with "A".
list = ["Kuldip", "Amar", "Akbar", "Mahesh", "Ramesh"]

for i in list:
    if i.startswith("A"):
        print(i)

'''
i.startswith("A"):
        print(i)  # it will give True or False 
'''

# Print numbers from 10 to 1 (in reverse using range()).
for i in range(10, 0, -1):
    print(i)

'''
basically range works like,
range(start, stop, step)

in this case,
for i in range(10, 0, -1)
it will start from 10
end from 1
-1 means loop decreases by 1 each time 
'''
    