# String is a data type in python.
# String is a sequence of characters enclosed in quotes.

# a ='harry'       
# Single quoted string 
# b = "harry"      
# Double quoted string 
# c = '''harry'''  
# Triple quoted string 

#           STRING SLICING 

# The index in a string starts from 0 to (length -1) in Python
#  In order to slice a string, we use the following syntax:

# name = "Areej"
# nameShort =name[0:4]
# start from index 0 all the way till 4 excluding 4
# character = name[4]
# 5thi character, indexing starts from 0
# print(character)
# print(nameShort)

#               SLICING WITH SKIP VALUE
word = "amazing" 
word[1: 6: 2] 

#               STRING FUNCTIONS 
# Now when operated on this string ‘str’, these functions do the following: 

 
# 1. len () function – This function returns the length of the strings. 
# str = "harry" 
# print(len(str))  # Output: 5 

# 2. String.endswith("rry") – This function_ tells whether the variable string ends with 
# the string "rry" or not. If string is "harry", it returns true for "rry" since Harry ends 
# with rry. 
# str = "harry" 
# print(str.endswith("rry"))  # Output: True 

 
# 3. string.count("c") – counts the total number of occurrences of any character. 
# str = "harry" 
# count = str.count("r") 
# print(count)  # Output: 2 

 
#  4. the first character of a given string. 
# str = "harry" 
# capitalized_string = str.capitalize() 
# print(capitalized_string)  # Output: "Harry" 


# 5. string.find(word) – This function friends a word and returns the index of first 
# occurrence of that word in the string. 
# str = "harry" 
# index = str.find("rr") 
# print(index)  # Output: 2 


# 6. string.replace (old word, new word ) – This function replace the old word with 
# new word in the entire string. 
# str = "harry" 
# replaced_string = str.replace("r", "l") 
# print(replaced_string)  # Output: "hally"

#               ESCAPE SEQUENCE CHARACTERS
# Escape Sequence characters comprise of more than one character but represent one 
# character when used within the strings
# Examples =>  \n , \t, \', \\


