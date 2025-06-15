''' Operators in Python:-
Operators are special symbols or keywords used to perform operations on variables and values.
They are used in arithmetic, comparison, logic, assignment, and more.
'''
'''
Arithmetic :	+, -, *, /, %, **, //	 
Assignment:	    =, +=, -=, *=
Comparison:	    ==, !=, >, <, >=, <=	
Logical:	    and, or, not	
Bitwise:	    &, `	
Membership:	    in, not in	
Identity:	    is, is not	
'''

# Examples

# Arithmetic operater
a = 22.2
b = 3
print("Addition is-->",a+b)
print("substraction is-->",a-b)
print("multipication is-->",a*b)
print("division is-->",a/b)
print("flor division is-->",a//b) # it will give int value if you use float..
print("power is-->",a**b)
print("modulo is-->",a%b)

# Comparison Operators
print("Is a equal to b?", a == b)
print("Is a greater than b?", a > b)


# Logical Operators
x = True
y = False
print("x and y:", x and y) # if any one is false they return False
print("x or y:", x or y)
print("not x:", not x)

# Membership Operators
name = "Kuldip"
print("Is 'u' in name?", 'u' in name) #check 'u' is in name or not
print("Is 'u' in name?", 'u' not in name) #return False

# Identity Operators
c = a
print("Is a same as c?", a is c) #True
print("Is a same as c?", a is b) #False

#Bitwise operater
'''Bitwise operators work on binary (bit-level) representations of integers.
They perform operations bit by bit — just like how numbers are handled in low-level programming or hardware.'''
a = 10  # In binary: 1010
b = 4   # In binary: 0100

print("a =", a)
print("b =", b)

print("Bitwise AND (a & b):", a & b)       # 1010 & 0100 = 0000 => 0
print("Bitwise OR (a | b):", a | b)        # 1010 | 0100 = 1110 => 14
print("Bitwise XOR (a ^ b):", a ^ b)       # 1010 ^ 0100 = 1110 => 14
print("Bitwise NOT (~a):", ~a)             # ~1010 = -(1010 + 1) = -11
print("Left Shift (a << 1):", a << 1)      # 1010 << 1 = 10100 => 20
print("Right Shift (a >> 1):", a >> 1)     # 1010 >> 1 = 0101 => 5


#Other examples

# Take two numbers from user input and perform all arithmetic operations.
a = int(input("Enter first no. -->"))
b = int(input("Enter second no. -->"))

print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a//b)
print(a%b) # it will give reminder
print(a**b) 

# Use comparison operators to compare age and print messages.
age1 = 20
age2 = 23
print("age1 is eqal to age2 -->",age1 == age2) #False
print("age1 is greater to age2 -->",age1 > age2) #False
print("age1 is lesser to age2 -->",age1 < age2) #True
print("age1 is not equal to age2 -->",age1 != age2) #False

# Use and, or, not to check login conditions.

x = True
y = False
print("x and y both login? ",x and y)
print("x or y any one is login? ",x or y)
print("x is login? ",not x)

# Check if a letter exists in a word using in.
word = "Hello soham"
print("word \'s\' is exist in word :", 's' in word)

# Use assignment operators like += and *= on a variable and print results.
x = 10
x += 5 # it will add 5 in x
print(x)

y = 10
y *= 10
print(y)

z = 10
z -= 5
print(z)