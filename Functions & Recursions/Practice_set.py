

# 1. Write a program using functions to find greatest of three numbers. 
# a = int(input('Enter a number : '))
# b = int(input('Enter a number : '))
# c = int(input('Enter a number : '))

# def greatest(a,b,c):
#     if a>b and a>c :
#         print(f"{a} is greatest")
#     if b>a and b>c :
#         print(f"{b} is greatest")
#     if c>a and c>b :
#         print(f"{c} is greatest")

# greatest(a,b,c)


# 2. Write a python program using function to convert Celsius to Fahrenheit. 
# C = int(input('Enter Temperature : '))
# def temp(C):
#     F = (C*(9/5))+32
#     print(F)
# temp(C)


# 3. How do you prevent a python print() function to print a new line at the end. 
# print("A")
# print("B")
# print("C",end="")
# print("D",end="")


# 4. Write a recursive function to calculate the sum of first n natural numbers. 
# n = int(input("Enter a number : "))
# i=1
# def sum_natural(n):
#     if n ==0 :
#         return 0
#     return n+sum_natural(n-1)

# print("Sum of first", n, "natural numbers is:", sum_natural(n))

# 5. Write a python function to print first n lines of the following pattern: 
'''
***
**
*
'''
#  for n = 3 
# n=int(input("Enter a number : "))
# i=1
# def star(n):
#     for i in range(1,n+1):
#         print("*"*((n+1)-i))        
        
# star(n)


# 6. Write a python function which converts inches to cms. 
# def inch_to_cms(inch):
#     return inch * 2.54

# n = int(input("Enter value in inches: "))

# print(f"The corresponding value in cms is {inch_to_cms(n)}")


# 7. Write a python function to remove a given word from a list and strip it at the same time. 
# def rem(l, word):
#     n = [] 
#     for item in l:
#         if not(item == word):
#             n.append(item.strip(word))
#     return n


# l = ["Harry", "Rohan", "Shubham", "an"]

# print(rem(l, "an"))

# 8. Write a python function to print multiplication table of a given number.
# n=int(input("Enter a number : "))
def multiply(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")

multiply(5)


# - Write a function to check if a number is prime.
# - Implement a function that returns the factorial of a number using recursion.	
# - Use map() to square all elements in a list.
# - Write a function that finds the largest element in a list.
# - Implement exception handling for division by zero.
