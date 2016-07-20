# There is NO variable in Python but only named references to objects and reference behave like lable allowing to retrieve objects 
x = 4 # this creates an int object (4) and assign it to x which is now a reference of the int object
print(x)

# this causes Python to create another int object and assign the new int object to x (which is the reference of the int 5)
# int is immutable in python; the 4 int object will be GCed.
x = 5  
print(x)

y = x # this copies the int object reference x to object reference y hence both x and y now refer to the same int object 5.
print(y)

y = 6 # this assigns the object reference y to a newly created int object 6; x is unaffected
print(y)

# built-in id() returns an unique object identifier but it's seldom used in production
print(id(x))
print(id(y))

# is operator is more commonly used than id() which tests equality of identity, that is whether two references refer to the same object! 
print(x is y) # test whether x and y refer to the same object 

# Assignment operator always binds to name; never copies object by value 
t = 4 # an int = 4 object is created and assigned to reference t 
t += 3 # another int object 3 is created and add it to int = 4 object; then assign the result (7) to reference t; 3 and 4 objects are now collectable 

# Value equality (or equivalent means the values of different objects are the same) is fundamentally different from identity!
# Value comparison can be controlled programatically; identity comparison is defined by the language and can't be changed
r = [1, 2, 3]
s = [1, 2, 3]
print('Value equality: ', r == s)
print('Identity comparison: ', r is s)

# function arguments and return result are by passed reference; no objects are copied!
def f1(x):
    x.append(4)
f1(s) # the object that s refers to is modified 
print(s)

def f2(x):
    return x
w = f2(s)
print(s is w) # identity comparision e.g. refer to the same object  

# optional argument
def banner(message, border = '-'):
    b = border * len(message) # repetition operation of string 
    print(b)
    print(message)
    print(b)

banner('Hello, Dragonfly')
banner('Chinese Red', '*')

# NOTE about default argument; def is a statement that when executed binds a funtion definition to a function name 
# and default argument value is only executed when def is evaluated. This causes no problem when using immutable type as 
# a default argument but if using mutable type e.g. a list it can cause serious problem since the argument is passed by reference 
# and it's kept in memory; it will be continuously modifed when the same function is called repeatedly.
def add_spam(x = []): # using a mutable type like list as default value can be problematic
    x.append('spam')
    return x

## doesn't work!
print(add_spam())
print(add_spam())

# the solution is using immutable type as default ValueError
def add_spam2(x = None):
    if x is None:
        x = []
    x.append('spam')
    return x

# now works!    
print(add_spam2())
print(add_spam2())

# For any language type system is one of the most important characteristics; Python is strongly and dynamically typed! 
def add(a, b): # here a and b can be any type that defines + operator
    return a + b

# dynamically typed as the types are resolved at runtime so all these work
add(3, 4)
add('3', '4')
add([3], [4])
add(3.4, 5.4)

# strongly typed e.g. there is no implicit conversion between types (unlike javascript) so this doesn't work. The exception is converting to bool! 
try:
    add('3', 4)
except TypeError:
    print('Python is strongly typed as doesnot automatically convert between types!')

# scopes in python are defined using LEGB (Local, Enbracing, Global, and Builtins)
# to use a global variable within a local scope; use 'global' keyword
# type can be used to determine the type of an object
# dir() can be used to introspect an object and get its attributes 

# everything in python is an object including int, string, module, function!!!
import words

print(type(words)) # get the type of a module; everything is an object!
print('Attributes of a module:', dir(words)) # get all attributes on an object including the ones imported and defined 

print(type(words.fetch_words)) # get type of a function 
print(dir(words.fetch_words)) # get all attributes of a function 
print(words.fetch_words.__code__) # get a particular attribute of a function 

