# Dictionary is a collection of keys-value pairs. 
# Syntax:   
# a = { 
# "key": "value", 
# "harry": "code", 
# "marks": "100", 
# "list": [1, 2, 9] 
# } 
# print(a["key"])  # Output: "value" 
# print(a["list"])  # Output: [1, 2, 9]


# PROPERTIES OF PYTHON DICTIONARIES
# 1. It is unordered. 
# 2. It is mutable. 
# 3. It is indexed. 
# 4. Cannot contain duplicate keys. 


# DICTIONARY METHODS 
# Consider the following dictionary. 
# a={"name":"harry" 
# "from":"india" 
# "marks":[92,98,96]}
 
# • a.items(): Returns a list of (key,value)tuples. 
# • a.keys(): Returns a list containing dictionary's keys. 
# • a.update({"friends":}): Updates the dictionary with supplied key-value pairs. 
# • a.get("name"): Returns the value of the specified keys (and value is returned 

# for eg
# marks={
#     "harry":"100",
#     "tom":"90",
#     "jerry":"80",
#     "jane":"90"
# }
# print(marks.get("harry"))
# print(marks["harry"])
# both return 100 but they are not the same.

# print(marks.get("tom1")) # prints none
# print(marks["tom1"]) #returns an error message

# EMPTY DICTIONARY
# e={}

# EMPTY SET
# e=set()

# SETS IN PYTHON. 
# Set is a collection of non-repetitive elements. 

# s={1,5,32}  syntax of a set

# set me koi bhu element repeat nahi hota hai.jb bhi humare paas aise elements hote h jo repeat nahi kr sakte toh hum set ka use krte h
#  set me order maintain nahi hota hai

# s = set() no repetition allowed! 
# s.add(1) 
# s.add(2)           
# or set ={1,2} 


# If you are a programming beginner without much knowledge of mathematical operations on sets, you can simply look at sets in python as data types containing unique values. 


# PROPERTIES OF SETS 
# 1. Sets are unordered => Element’s order doesn’t matter 
# 2. Sets are unindexed => Cannot access elements by index 
# 3. There is no way to change items in sets. 
# 4. Sets cannot contain duplicate values. 



# OPERATIONS ON SETS 
# Consider the following set: 
# s = {1,8,2,3} 
# • len(s): Returns 4, the length of the set  
# • s.remove(8): Updates the set s and removes 8 from s. 
# • s.pop(): Removes an arbitrary element from the set and return the element removed. 
# • s.clear():empties the set s. 
# • s.union({8,11}): Returns a new set with all items from both sets. {1,8,2,3,11}. 
# • s.intersection({8,11}): Return a set which contains only item in both sets  {8}. 