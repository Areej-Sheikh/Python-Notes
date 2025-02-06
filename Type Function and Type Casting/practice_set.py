# 1. Write a python program to add two numbers.
# 2. Write a python program to find remainder when a number is divided by z. 
# 3. Check the type of variable assigned using input () function. 
# 4. Use comparison operator to find out whether ‘a’ given variable a is greater than ‘b’ or not. Take a = 34 and b = 80 
# 5. Write a python program to find an average of two numbers entered by the user. 6. Write a python program to calculate the square of a number entered by the user. 


# 1
a=15
b=10
sum = a+b
print(sum)


# 2
a=32
b=13
remainder = a % b
print(remainder)

# 3
num = input("Enter a number: ")
print("The type of variable assigned is: ", type(num))

# 4
a=34
b=80
if (a>b):{
    print("a is greater than b")
}
else:{
    print("b is greater than a")
}

# 5
a=23
b=50
average = (a+b)/2

print("The average of",a,"and",b,"is:",average)