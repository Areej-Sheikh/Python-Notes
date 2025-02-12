

# Map Function
# Use map() to square all elements in a list.
# x = [1, 2, 3, 4, 5]
# def square(x):
#     return x*x
# n=list(map(square,x))
# print(n)

# Use map() to double all elements in a list.
# l=[1,2,3,4,5,6,7,8,9,10]
# def double(x):
#     return x*2
# newlist=list(map(double,l))
# print(newlist)

# Use map() to convert a list of strings to uppercase.
# s="this is a new sring"
# upper_list = list(map(str.upper, s.split()))
# print(upper_list)

# Filter Function
# Use filter() to extract even numbers from a list.
# l=[1, 4, 9, 16, 25, 36, 49, 64, 81]
# evens = filter(lambda x: x % 2 == 0, l)
# print(list(evens))

# Use filter() to find numbers greater than 10 in a list.
# l=[1, 4, 9, 16, 25, 36, 49, 64, 81]
# def greater(l):
#     return l>10
# newlist = list(filter(greater,l))
# print(newlist)


# Use filter() to extract words longer than 5 characters from a list of strings.
# s="this is another string"
# long=list(filter(lambda word:len(word)>5,s.split()))
# print(long)

# Reduce Function
from functools import reduce

# Use reduce() to find the sum of all elements in a list.
# l=[1,2,3,4,5,6,7,8,9,10]
# sum = reduce(lambda x, y: x + y, l)
# print(sum)

# Use reduce() to find the product of all elements in a list.
# l=[1, 4, 9]
# p = reduce(lambda x, y: x * y, l)
# print(p)

# Use reduce() to find the maximum element in a list.
# l=[ 5, 63,78, 49,12 ,88,64, 81]
# e=reduce(lambda x, y: x if x > y else y, l)
# print(e)
