'''
1. break Keyword:
The break statement is used to exit the loop immediately, even if the loop condition is still True.
'''

# Example 
for i in range(1, 11):
    if i==5:
        break # It will stop the loop when 5 number is reach.(5 not print)
    print(i, end=" ")

# Output will be, 1 2 3 4

'''
2. continue Keyword:
The continue statement skips the current iteration and goes to the next one.
'''
for i in range(1,11):
    if i==5:
        continue #It will skip number 5 
    print(i, end=" ")

# # Output will be, 1 2 3 4 6 7 8 9 10

'''
pass Keyword:
The pass statement is a placeholder — it does nothing and is used when a statement is syntactically required but you don’t want to write any code yet.
'''

# Example
for i in range(3):
    if i == 1:
        pass # Will add logic latter
    else:
        print(i) 

# Output will be, 0 2

# Some Practice Questions

# Keep asking the user for input and break the loop if the user enters "exit".
while True:
    name = input("Enter some input -->")

    if name == "exit":
        break

# print numbers from 1 to 20 but stop when a number is divisible by 7.
for i in range(1,21):
    if i%7==0:
        break
    else:
        print(i)

# Print all numbers from 1 to 20 except multiples of 4.
for i in range(1,21):
    if i%4==0:
        continue
    else:
        print(i, end=" ")

# Loop through a string and skip vowels while printing consonants.
str = "kuldip"
vowvwls = "aeiouAEIOU"
for i in str:
    if i in vowvwls:
        continue
    print(i, end=" ")

# Use pass inside an if block where you plan to add logic later.
for i in range(1,11):
    if i == 2:
        pass
    else:
        print(i)

#Create a loop through a list of usernames and use pass for invalid entries (e.g., empty strings).
usernames = ["kuldip", " ", "kenil", " ", "gautum"]

for i in usernames:
    if i==" ":
        pass
    else:
        print(i)