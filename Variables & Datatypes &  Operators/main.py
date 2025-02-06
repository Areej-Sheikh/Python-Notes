# Variables are containers that store information that can be manipulated and referenced later by the programmer within the code.

# In python, the programmer does not need to declare the variable type explicitly, we just need to assign the value to the variable.

#           Primarily these are the following data types in Python:
# 1. Integers 
# 2. Floating point numbers
# 3. Strings 
# 4. Booleans  
# 5. None 


#           RULES FOR CHOOSING AN IDENTIFIER 
# • A variable name can contain alphabets, digits, and underscores. 
# • A variable name can only start with an alphabet and underscores. 
# • A variable name can’t start with a digit. 
# • No while space is allowed to be used inside a variable name. 
# Variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable name must start with a letter or the underscore character.
# Variables are case sensitive.
# Variable name cannot start with a number.

# name = "Abhishek"   #type str
# age = 20            #type int
# passed = True       #type boolean

# It is always advisable to keep variable names descriptive and to follow a set of conventions while creating variables:


# Local Variable:
# A local variable is created within a function and can be only used inside that function. Such a variable has a local scope.

# icecream = "Vanilla"    #global variable
# def foods():
#     vegetable = "Potato"    #local variable
#     fruit = "Lichi"         #local variable
#     print(vegetable + " is a local variable value.")
#     print(icecream + " is a global variable value.")
#     print(fruit + " is a local variable value.")

# foods()

# Global Variable:
# A global variable is created in the main body of the code and can be used anywhere within the code. Such a variable has a global scope.

# icecream = "Vanilla"    #global variable
# def foods():
#     vegetable = "Potato"    #local variable
#     fruit = "Lichi"         #local variable
#     print(vegetable + " is a local variable value.")

# foods()
# print(icecream + " is a global variable value.")
# print(fruit + " is a local variable value.")



# OPERATORS IN PYTHON Following are some common operators in python:
#  1. Arithmetic operators: +, -, *, / etc. 
# 2. Assignment operators:  =, +=, -= etc.
#  3. Comparison operators: ==, >, >=, <,  != etc. 
# 4. Logical operators: and, or, not. 