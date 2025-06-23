# String methods and function 
'''
In Python, string methods are built-in functions that you can use with strings to manipulate, analyze, or transform them.

Strings are immutable, so methods often return a new string
'''

# Common String Methods with Example

# 1. .lower() ,converts in lowercase
word = "HELLO"
print(word.lower()) # hello

# 2. .upper() ,converts in uppercase
word = "hello"
print(word.upper()) # HELLO

# 3. .capitalize() ,Capitalize the first letter
word = "hello"
print(word.capitalize()) # Hello

# 4. .title() ,Capitalizs first letter of each word
word = "hello world. how are you?"
print(word.title()) # Hello World. How Are You?

# 5. .strip , Remove spaces from both ends
word = " hello "
print(word.strip()) #hello

# 6. .replace(old, new) ,Replace substrings
word = "Hello world"
print(word.replace("world", "Python")) # Hello Python

# 7. .find() ,return the index of first occurrence
word = "Hello"
print(word.find("o")) # 4

# 8. .count() ,Counts how many times a substring appears
word = "hello"
print(word.count("l")) #2

# 9. .startwith() / .endwith() ,check Start or End
word = "Good Morning"
print(word.startswith("G")) #True
print(word.endswith("ng")) #True

# 10. .split() ,Splits a string into a list
word = "Apple, Banana, Graps"
print(word.split(",")) #['Apple', ' Banana', ' Graps'] , It will convert into list by (,) seprated


# Practice Questions 

# Convert a user-entered sentence to all lowercase and all uppercase.
str = input("Enter a String -->")
print(str.upper())
print(str.lower())

# Count how many times the letter "e" appears in a word.
str = "My name is jethalal"
print(str.count("e"))

# Replace all spaces with hyphens in a sentance
sentance = "Good Morning!"
print(sentance.replace(" ","-"))

# Ask the user for a name and check if it is starts with "A".
ask = input("Enter Your Name -->")
print(ask.startswith("A"))

# Remove leading and trailing spaces from user input using .strip().
sentance = " Good Morning! "
print(sentance.strip())

# Split a comma-separated string into a list of words.
str = "Asus,lenavo,Macbook"
print(str.split(","))

# Count how many words are in sentence using .split() and len().
word = "good morning"
split = word.split()
count = len(split)
print(count)

# Ask the user to input an email and check if it ends with "@gmail.com".
Ask = input("Enter an email -->")
print(Ask.endswith("@gmail.com"))

# Capitalize the first letter of each word in a sentence.
sentence = "good morning"
print(sentence.title())

# Take a string and remove all vowels using .replace() in a loop.
str = input("Enter a string -->")
vowels = "aeiouAEIOU"
for i in vowels:
    str = str.replace(i,"")

print(str)

