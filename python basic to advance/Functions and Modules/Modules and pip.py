# Modules
'''
A module in Python is simply a file containing Python code (functions, classes, variables) that you can reuse in other programs using the import statement.
'''

'''
Types of Modules:
Built-in modules : Provided by Python (e.g., math, random, datetime)

User-defined modules : Python files you create

Third-party modules : Installed using pip (e.g., numpy, requests, pandas)
'''

# Example: Using a Built-in Module
import math

print(math.sqrt(17))
print(math.pi)

# Example: Creating and Using a User-Defined Module

# this module was taken from another file which name is "my_intro"
import my_intro

my_intro.intro("mohan")

#  from ... import ...
from math import sqrt

print(sqrt(5))


# pip
'''
pip stands for Pip Installs Packages.
It’s Python’s tool for installing third-party libraries from PyPI (Python Package Index).
'''

'''
| Command                         | Description                  |
| ------------------------------- | ---------------------------- |
|  pip install packagename        | Install a package            |
|  pip uninstall packagename      | Uninstall a package          |
|  pip list                       | List all installed packages  |
|  pip show packagename           | Show package details         |
|  pip freeze > requirements.txt  | Save environment for sharing |

'''
