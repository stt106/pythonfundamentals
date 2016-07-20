# string in python is of type str which is a homogeneous (of the same type!) immutable sequence of unicode codepoints (characters)

print(len('hello dragonfly close!')) # length of string

s = "hello"
s += " world" # using too much += will cause memory issue as strings are immutable!

# using join() on str is more memory efficient to join a list of large number of strings together
sentence = ','.join(['hello there', 'what'' your name?', 'what? you don''t want to tell me?'])
''.join(['abc', 'def', 'jjjjjjjjjjjj']) # using empty string as the separator to efficiently join multiple strings! something from nothing!
print(sentence)
splits = sentence.split(',') # splits the string back to a list 
print(splits)

# partition returns a tuple of 3 parts of the string: prefix, separator, suffix; using _ as a dummy variable 
origin, _, destination = "Zhuanghe-London".partition('-') 
print(origin, destination)

# format function on str
print("The age of {0} is {1}".format('Rita', 26))
print("The age of {} is {}".format('Mandy', 33)) # if arguments are used in sequence they can be omitted

 # named fields are matched with the keyword arguments; order is not important 
print("Current month and day: {month} the {day}".format(day = "17th", month="July")) 

pos = (23.4, 59.5, 69.5)
# access values through keys or indexes with curely bracket in the replacement field 
print("Galactic position x = {pos[0]}, y = {pos[1]}, z = {pos[2]}".format(pos=pos))

# it's ok to pass in a whole module
import math
print("Math constants: pi = {m.pi:.3f}, e = {m.e}".format(m = math)) # passing in math; also note the alignment formatting options 
