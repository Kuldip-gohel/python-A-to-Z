# Match_case statement
'''
The match-case statement in Python (introduced in Python 3.10) is similar to the switch-case statement in other programming languages.
It allows you to match a value against multiple cases and execute code based on the match.
'''

# Syntax:
'''
match variable:
    case value1:
      # code block
    case value2:
      # code block
    case _:
       # default case (like "else")
'''

# Example
Day = input("Enter a day, I will give you which day of gym is-->")

match Day:
    case "monday":
        print("This is a chest day")
    case "tuesday":
        print("This is a Arms day")
    case "wednesday":
        print("This is a Pack day")
    case "Thursday":
        print("This is a Back day")
    case "Friday":
        print("This is a Lage day")
    case "Saturday":
        print("This is a Another excersize day")
    case _:
        print("Its a Rest day")

# Another examples of Match_case 

# Match numbers from 1 to 5 and print number names.

number = input("Enter number i will give you its name -->")
match number:
    case "1":
        print("You enter a one number ")
    case "2":
        print("You enter a Two number ")
    case "3":
        print("You enter a Three number ")
    case "4":
        print("You enter a Four number ")
    case "5":
        print("You enter a Five number ")
    case _:
        print("Please Enter number betwwen 1 to 5")

# Build a basic calculator using match-case for operations (+, -, *, /).

num1 = int(input("Enter first number  -->"))
operater = input("Enter operater (+, -, *, /):")
num2 = int(input("Enter second number  -->"))


match operater:
    case "+":
        print("Addition is -->",(num1+num2))
    case "-":
        print("Addition is -->",(num1-num2))
    case "*":
        print("Addition is -->",(num1*num2))
    case "/":
        print("Addition is -->",(num1/num2))
    case _:
        print("Enter a valid operater ")
    

# Match a user role (admin, editor, viewer) and print their access level.

user = input("Enter Your role -->")
match user:
    case "admin":
        print("You Can Access every thing")
    case "editor":
        print("You Can Access editing tools only")
    case "viewer":
        print("You Can Access only our Servises")
    case _:
        print("Please Enter Valid Role")


# Take a grade as input (A, B, C, etc.) and print performance.

grade = input("Please Enter your grade -->")
match grade:
    case "A":
        print("Your Performance is Excilent")
    case "B":
        print("Your Performance Much Batter")
    case "C":
        print("Your Performance is Batter")
    case "D":
        print("Your Performance is Good")
    case _:
        print("Keep learning and achive batter performance")
