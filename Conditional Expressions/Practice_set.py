
# 1. Write a program to find the greatest of four numbers entered by the user. 
a = int(input("Enter a number1"))
b = int(input("Enter a number2"))
c = int(input("Enter a number3"))
d = int(input("Enter a number4"))

if a > b and a > c and a > d:
    print(f"{a} is the greatest number.")

elif b > a and b > c and b > d:
    print(f"{b} is the greatest number.")

elif c > a and c > b and c > d:
    print(f"{c} is the greatest number.")

elif d > a and d > b and d > c:
    print(f"{d} is the greatest number.")

else:
    print("All numbers are equal.")


# 2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user. 
marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))

# Check for total percentage
total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed:", total_percentage)

else:
    print("You failed, try again next year:", total_percentage)


# 3. A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams. 
p1 = "Make a lot of money"
p2 = "buy now"  
p3 = "subscribe this"  
p4 = "click this"

message = input("Enter your comment: ")

if((p1 in message) or (p2 in message )or (p3 in message) or (p4 in message)):
    print("This comment is a spam")

else:
    print("This comment is not a spam")

# 4. Write a program to find whether a given username contains less than 10 characters or not. 
username = input("Enter username: ")

if(len(username)<10):
    print("Your username contains less than 10 characters")
else:
    print("Your username contains more than or equal to 10 characters")


# 5. Write a program which finds out whether a given name is present in a list or not. 
l = ["Harry", "Rohan", "Shubham", "Divya"]

name = input("Enter your name: ")

if(name in l):
    print("Your name is in the list")
else:
    print("Your name is not in the list")


# 6. Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50 => F 
marks = int(input("Enter your marks: "))

if(marks<=100 and marks>=90):
    grade = "Ex"
elif(marks<90 and marks>=80):
    grade = "A"
elif(marks<80 and marks>=70):
    grade = "B"
elif(marks<70 and marks>=60):
    grade = "C"
elif(marks<60 and marks>=50):
    grade = "D"
elif(marks<50):
    grade = "F"

print("Your grade is:", grade)


# 7. Write a program to find out whether a given post is talking about “Harry” or not.
post = input("Enter the post: ")



if("harry" in post.lower()):
    print("This post is talking about harry")

else:
    print("This post is not talking about harry")



# Write a program that checks if a number is positive, negative, or zero using If-Else.



# Create a function that takes a number as input and returns "Even" or "Odd".



# Write a Python program to print numbers from 1 to 10 using a While Loop.



# Use a For Loop to print the sum of all even numbers from 1 to 50.



# Implement a function that calculates the factorial of a given number.