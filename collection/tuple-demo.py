# Tuples are hetergeneous (of different types) immutable sequence; once created objects/items within it can not be replaced or removed; new elements cannot be added!

t = ("dragonfly", 3.4, 1, True) # create a tuple 

print(t[2]) # 0 based index

print(len(t)) # get the length of tuple

for i in t:
    print(i) # iterate tuple 

print(t + ("close", [1,2,3])) # concatenate tuples; note that tuple can containe any type even list!

print(t * 2) # repetition on tuple; note that t is immutable so concatenation didn't modify it 

print((1,'hi', ('there', 2))) # nested tuple is perfectly fine

print(type((3,))) # single element tuple, using trailing comma 
print(()) # empty tuple 

p = 1, 2, 3 # create a tuple; () is optional 
print(type(p))

def minmax(items):
    return min(items), max(items) # return a tuple 

lower, upper = minmax([1,2 ,3, 4, 5]) # tuple unpacking allows to destructure directly into named references 
print(lower, upper)

(a, (b, (c, d))) = (4, (3, (1, 2))) # tuple unpacking works with nested tuples though not other data types 
print(a, b, c, d)

def swap(a, b):
    return b, a # note this returns a tuple! so swapping two variables are dead easy in Python!
print(swap('a', 'b'))
print(swap(1, 2))

# tuple ctor
print(tuple([1, 2, 3, 49, 199])) # convert list to tuple 
print(tuple("hello there")) # convert string (which is list of string) to tuple 

print(4 in (1, 2, 3, 4)) # test existance
print(4 not in (1, 2, 3))
