# A function is a group of statements performing a specific task. 
# When a program gets bigger in size and its complexity grows, it gets difficult for a program to keep track on which piece of code is doing what! 
# A function can be reused by the programmer in a given program 


# EXAMPLE AND SYNTAX OF A FUNCTION 

# The syntax of a function looks as follows: 
# def func1(): 
# print('hello') 

# This function can be called any number of times, anywhere in the program. 


# FUNCTION CALL 
# Whenever we want to call a function, we put the name of the function followed by parentheses as follows: 
# func1() # This is called function call. 

# function to find the average of 3 numbers:
# def avg():
#     a=int(input("Enter a number : "))
#     b=int(input("Enter a number : "))
#     c=int(input("Enter a number : "))
#     average = (a+b+c)/3
#     print(average)

# avg() #function bieng called

# FUNCTION DEFINITION 
# The part containing the exact set of instructions which are executed during the function call.
 
# Quick Quiz:  Write a program to greet a user with “Good day” using functions. 
# name = input("Enter your name : ")
# def greet():
#     print(f"Greetings! {name}")

# greet()

# TYPES OF FUNCTIONS IN PYTHON 
# There are two types of functions in python: 
# • Built in functions (Already present in python) 
# • User defined functions (Defined by the user) 

# Examples of built in functions includes len(), print(), range() etc. 
# The func1() function we defined is an example of user defined function. 


# FUNCTIONS WITH ARGUMENTS 
# A function can accept some value it can work with. We can put these values in the parentheses. 
# A function can also return value as shown below:
# def greet(name,ending="Thankyou"):
#     print("Greetings!"+ name)
#     print(ending)
#     return

# a=greet("Areej","Thankyou for visiting!")
# print(a)

# DEFAULT PARAMETER VALUE 
# We can have a value as default as default argument in a function. 
# If we specify name = “stranger” in the line containing def, this value is used when no argument is passed. 

# Example: 
# def greet(name = "stranger"): 
# function body 
# greet() # name will be "stranger" in function body (default) 
# greet("harry") # name will be "harry" in function body (passed) 


# RECURSION 
# Recursion is a function which calls itself. 
# It is used to directly use a mathematical formula as function.  

# Example: 
# factorial(n) = n x factorial (n-1) 
# This function can be defined as follows: 

# def factorial(n):
#     if i == 0 or i==1: # base condition which doesn’t call the function any further 
#         return 1 
#     else: 
#         return n*factorial(n-1) # function calling itself 


'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 X 1
factorial(3) = 3 X 2 X 1
factorial(4) = 4 X 3 X 2 X 1
factorial(5) = 5 X 4 X 3 X 2 X 1
factorial(n) = n X n-1 X......3 X 2 X 1

factorial(n) = n * factorial(n-1)
.
.
.
.
.
.
.
factorial(5)= 5 x factorial(4)
factorial(5)= 5 x 4 x factorial(3)
factorial(5)= 5 x 4 x 3 x 2 x factorial(2)
factorial(5)= 5 x 4 x 3 x 2 x factorial(1)
factorial(5)= 5 x 4 x 3 x 2 x 1

Hence:
factorial(n) = n * factorial(n-1)

'''

# def factorial(n):
#     if(n==1 or n==0):
#         return 1
#     return n * factorial(n-1)


# n = int(input("Enter a number: "))
# print(f"The factorial of this number is: {factorial(n)}")
        
# The programmer needs to be extremely careful while working with recursion to ensure that the function doesn’t infinitely keep calling itself. 
# Recursion is sometimes the most direct way to code an algorithm. 


# LAMBDA FUNCTION IN PYTHON
# In Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword and has the following syntax:

# lambda arguments: expression

# Lambda functions are often used in situations where a small function is required for a short period of time. They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.

# Here is an example of how to use a lambda function:

# Function to double the input
# def double(x):
#   return x * 2

# Lambda function to double the input
# lambda x: x * 2

# Function to calculate the avg of two numbers, cube of a number and square of a number can also be done as:

# double=lambda x:x*x
# cube=lambda x:x*x*x
# avg=lambda x,y:(x+y)/2

# print(f"Double ={double(5)}")
# print(f"Cube ={cube(9)}")
# print(f"Avg = {avg(10,31)}")

# The above lambda function has the same functionality as the double function defined earlier. However, the lambda function is anonymous, as it does not have a name.

# Lambda functions can also include multiple statements, but they are limited to a single expression. For example:

# Lambda function to calculate the product of two numbers, with additional print statement
# lambda x, y: print(f'{x} * {y} = {x * y}')

# In the above example, the lambda function includes a print statement, but it is still limited to a single expression.

# Lambda functions are often used in conjunction with higher-order functions, such as map, filter, and reduce which we will look into later.





