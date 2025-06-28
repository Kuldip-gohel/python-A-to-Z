# Dictionary
'''
A dictionary is a collection of key-value pairs.
It is unordered, mutable, and does not allow duplicate keys.
- Created using curly braces {}
- Keys must be unique and immutable (like strings, numbers, tuples)
- Values can be any type
'''

# Example
Student = {
    "name":"kuldip",
    "age":20,
    "grade":"A"
}
print(Student)  #{'name': 'kuldip', 'age': 20, 'grade': 'A'}

# Accessing and Modifying Dictionary
print(Student["name"]) #kuldip
Student["age"] = 21
Student["Collage"] = "GTU"
print(Student)

# Useful Dictionary Methods
'''
| Method      | Description                                         | Example                       |
| ----------- | --------------------------------------------------- | ----------------------------- |
|  .get(key)  | Returns value for key (returns `None` if not found) |  student.get("age")           |
|  .keys()    | Returns all keys                                    |  student.keys()               |
|  .values()  | Returns all values                                  |  student.values()             |
|  .items()   | Returns all key-value pairs                         |  student.items()              |
|  .update()  | Updates dictionary with another dictionary          |  student.update({"age": 23})  |
|  .pop(key)  | Removes key and returns its value                   |  student.pop("grade")         |
|  .clear()   | Removes all items                                   |  student.clear()              |
|  .copy()    | Returns a shallow copy                              |  new_dict = student.copy()    |
'''

# Looping Through Dictionary
for key, value in Student.items():
    print(f"{key} → {value}")

# Dictionary from List of Tuples
info = [("name", "Kuldip"), ("age", 21)]
my_dict = dict(info)
print(my_dict) #{'name': 'Kuldip', 'age': 21}

#  Practice Questions

# Create a dictionary to store information of a student (name, age, grade).
Student = {
    "name":"Mohan",
    "age":22,
    "grade":"A"
}

# Add a new key course to the dictionary.
Student["course"] = "BSC IT"
print(Student)

# Update the student's age.
Student["age"] = 23
print(Student)

# Remove the key grade using .pop().
Student.pop("grade")
print(Student)

# Loop through the dictionary and print all keys and values.
for key,value in Student.items():
    print(f"{key} -> {value}")

# Count the number of keys in a dictionary using len().
len = len(Student)
print(len)

# Merge two dictionaries using .update().
Dict1 = {
    "Name":"Sohan",
    "age":22,
    "course":"VNSGU"
}

Dict2 = {
    "Weight":"54 Kg",
    "Height":"170 cm",
    "Gender":"Male"
}
Dict1.update(Dict2)
print(Dict1) 
#{'Name': 'Sohan', 'age': 22, 'course': 'VNSGU', 'Weight': '54 Kg', 'Height': '170 cm', 'Gender': 'Male'}

# Create a dictionary from two lists: one of keys, one of values.
Keys = ["name","age","course"]
Values= ["Rohan",22,"BCA"]

my_dict = dict(zip(Keys, Values))
print("Dictionary from lists:", my_dict)

# Use .get() to access a value without causing an error if the key is missing.
print(Student.get("age"))
print(Student.get("gender","N/A")) #N/A, If key is missing.

# Create a dictionary where keys are numbers from 1 to 5 and values are their squares.
squares = {}
for i in range(1, 6):
    squares[i] = i ** 2
    
print("Squares dictionary:", squares)

