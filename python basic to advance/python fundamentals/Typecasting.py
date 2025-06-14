'''Typecasting is a process of converting one data type to another. This are functions given for type cast like..'''
'''
int() → convert to integer
float() → convert to float
str() → convert to string
bool() → convert to boolean
'''

# Converting string to integer
num = "10" #string
num_int = int(num) # convert into int
print(num_int)

# Converting int to string
num = 20 #int
num_str = str(num) #int to str
print(num_str)
print(type(num_str)) #<class 'str'>

#Convert int to float
num = 20 #int
num_float = float(num) # int to float
print(num_float)
print(type(num_float)) #<class 'float'>

# Convert float to int
num_flo = 20.22  #float
num_int = int(num_flo) #float to int
print(num_int)
print(type(num_int)) #<class 'int'>

'''Using type casting we can convert any datatypes, according to need'''

# for example we have list and we want to convert their all elements into int...
list = [20.2,22.2,25.32,65.52]
for i in list:
    print(int(i))

'''Also we can do type casting in dictnory, set and many more according to our need'''

# Also we can convert Booleans into any datatypes
name = False
name_int = int(name)
print(name_int)
print(type(name_int))