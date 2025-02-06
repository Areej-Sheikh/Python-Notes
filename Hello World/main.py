#this is a program to print hello world
# print('hello world!')

# single line comment ==>
# this is a comment

"""this
is a
 multiline
comment"""


# this is how to use an external module in our code
import pyttsx3
engine = pyttsx3.init()
engine.say('hi this module is used for text to speech recognition')
engine.runAndWait()