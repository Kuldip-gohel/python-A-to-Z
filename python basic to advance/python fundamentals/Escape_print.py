# Escape sequense
'''Escape sequences are special characters used inside strings to represent certain whitespace or formatting characters.
They start with a backslash \.'''

'''
Common Escape Sequences:

\n	New line	
\t	Tab (horizontal space)	
\\	Backslash	
\"	Double quote	
\'	Single quote	

'''

# Example
name = "kuldip"
age = 20
print("Name: ",name)
print("age: ",age)

#using escape sequence
print("Hello\nwelcome to python") # new line
print("Hello\tkuldip") #tab spase
print("Hello\"welcome\" to python")  #quote in text
print("This is backslash: \\") #backslash

# other examples

#1. Print your name and city on two lines using \n.
print("My name is kuldip\nI live in surat")

# 2. Format a product list using \t 
print("Product name is sugar,\tprice is 40")

# 3. Print a sentence that includes both single and double quotes.
print("oh! wow you are a \"Volyball player\". that is nice")

# 4. Print a file path like: C:\Users\YourName\Documents using \\.
print("C:\\Users\\YourName\\Documents")


'''Print statement'''
'''
The print() function is used to display output on the screen
'''

# Example
print("Hello world")


# you can print text, numbers, variables, or expressions.
# You can also customize it using parameters like sep, end.

print("your name is ",end='')
print("kuldip")