'''
Indexing:
Indexing is used to access individual characters in a string using their position (index).
Indexing starts at 0 (first character)
Negative indexing starts from -1 (last character)
'''

# Example

name = "kuldip"
print(name[0]) # k
print(name[3]) # d
print(name[-1]) # p
print(name[-4]) # l

# Slicing
'''
Slicing is used to extract a portion (substring) of a string
'''

# Syntax
'''
string[start : end : step]

'''

#Example
word = "pythonprograming"
print(word[0:10]) # pythonprog
print(word[5:11]) #nprogr
print(word[:11]) #pythonprogr
print(word[5:]) #nprograming
print(word[:-1]) #pythonprogramin
print(word[-1:]) # g
print(word[::2]) #ptopormn (Every second char)
print(word[::-1]) #gnimargorpnohtyp (reversed)

# Practice Questions 

# Print the first and last character of a string.
str = "Hello World"
print(str[0])
print(str[-1])

# Print only the middle part of a string (remove first and last).
str = "hello world"
print(str[1:-1])

# Reverse a string using slicing.
str = "ecnalubmA"
print(str[::-1])

# Print every second character of a string.
str = "helloworld"
print(str[1::2])

# Take a string input and print only the first 3 characters.
str = input("Enter a string -->")
print(str[:3])

# Slice and print the last 4 characters of a string.
str = "Helloworld"
print(str[-4:])

# Check Whether a String is a Palindrome Using Slicing
word = "abcba"
if word == word[::-1]:
    print("Palidrom")
else:
    print("Not Palidrom")

# Print Characters at Even Indexes
word = "kuldip"
print(word[::2])

