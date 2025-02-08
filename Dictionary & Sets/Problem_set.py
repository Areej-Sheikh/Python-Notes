# 1. Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up! 
# words ={
#     "help":"madat",
#     "cat":"billi",
#     "flower":"phool"
# }
# word = input('Please enter the word you want meaning of : ')
# print(words[word])

# 2. Write a program to input eight numbers from the user and display all the unique numbers (once). 
# s=set()
# n = input('Please enter the number you want : ')
# s.add(int(n))
# n1 = input('Please enter the number you want : ')
# s.add(int(n1))
# n2 = input('Please enter the number you want : ')
# s.add(int(n2))
# n3 = input('Please enter the number you want : ')
# s.add(int(n3))

# print(s)

# 3. Can we have a set with 18 (int) and '18' (str) as a value in it? 
# s=set()
# s.add(18)
# s.add('18')
# print(s)

# 4. What will be the length of following set s: 
# s = set() 
# s.add(20) 
# s.add(20.0) 
# s.add('20') # length of s after these operations? 
# length is 2 bec acc to python 20==20.0 


# 5. s = {}  What is the type of 's'? 
# it is a dictionary


# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
# d={}
# name = input('Enter name : ')
# language = input('Enter language : ')
# d.update({name:language})

# name = input('Enter name : ')
# language = input('Enter language : ')
# d.update({name:language})

# name = input('Enter name : ')
# language = input('Enter language : ')
# d.update({name:language})

# name = input('Enter name : ')
# language = input('Enter language : ')
# d.update({name:language})

# print(d)

# 7. If the names of 2 friends are same; what will happen to the program in problem 6? 
# the value will be updated again and no new entries will be created

# 8. If languages of two friends are same; what will happen to the program in problem 6? 
#  key cannot be same but values can be same so no difference

# 9. Can you change the values inside a list which is contained in set S? 
# s = {8, 7, 12, "Harry", [1,2]} 
# we cannot include a list in a set
#  there is no indexing in set so we cant change it


# Create a set with unique elements from a list of numbers with duplicates.


# Write a program to find the union and intersection of two sets.


# Create a dictionary with student names as keys and their marks as values. Print all student names who scored above 80.


# Write a function that takes a dictionary and returns a new dictionary with keys and values swapped.


# Implement a program that removes duplicate values from a dictionary.

