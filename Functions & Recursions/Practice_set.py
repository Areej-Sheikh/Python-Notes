

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
# def multiply(n):
#     for i in range(1, 11):
#         print(f"{n} X {i} = {n*i}")

# multiply(5)


# Write a function to check if a number is prime.
# def isPrime(n):
#     for i in range(2,n):
#         if(n%i)==0:
#             print("Number not is Prime")
#             break
#     else:
#         print("Number is Prime")
            
# isPrime(3)

# Implement a function that returns the factorial of a number using recursion.
# def factorial(n):
#     if n == 0 or n == 1:  # Base case
#         return 1
#     return n * factorial(n - 1)


# print(factorial(5))
        


# Write a function that returns the square of a number using the return statement.
# def square(n):
#     return n*n
# print(square(20))


# Implement a function with both local and global variables.
# counter = 10  # Global variable

# def update():
#     global counter
#     counter += 5  # Modify global variable
#     local_var = 3  # Local variable
#     print(counter, local_var)

# update()



# Write a function that finds the largest element in a list.
# def find_largest(lst):
#     if not lst: 
#         return None
#     return max(lst)

# numbers = [3, 7, 2, 9, 5]
# print(find_largest(numbers)) 
    
    




# RECURSION PRACTICE QUESTIONS

# Find the product of first n natural numbers using recursion.
# def product(n):
#     if n<0:
#         print('invalid input')
#     if n == 1 or n==0:
#         return 1
#     return n*product(n-1)

# number = product(5)
# print(number)    

# calculate the sum of digits of a number?
# def sum_digits(n):
#     if n < 10:  # Single-digit number
#         return n
#     return (n % 10) + sum_digits(n // 10)
# number = sum_digits(1234)
# print(number)

# check if a string is a palindrome
# Example: "madam"
# def palindrome(s):
#     if len(s)<2:
#         return True
#     if s[0]!= s[-1]:
#         return "Not a palindrome"
#     return palindrome(s[1:-1])
# print(palindrome("madam"))

# Reverse a String using Recursion
# def recursion(s):
#     if len(s)<2:
#         return s
#     return  s[-1] + recursion(s[:-1])
# print(recursion("heaven"))

# write a recursive function to count the number of digits in a number?
# def count(n):
#     if n<10:
#         return 1
#     return 1+ count(n//10)

# number = count(1234)
# print(number)