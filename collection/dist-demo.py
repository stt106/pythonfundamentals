# dict = unordered mapping from unique, immutable keys (string, int, tuples are fine but list are not!) to mutable values; dict itself is mutable!
# should never depend on the order of elements in the dist; the order in theory is random 

# dict ctor
names_and_ages = [('Alice', 33), ('Rita', 25), ('Mandy', 33)]
d = dict(names_and_ages) # convert a list of tuples into dict
print(d) 

# as long as keys are legitimate Python identifiers, it's even possible to create a dictionary directly from keyword argument passed the dict
phonetic = dict(a = "alfa", b = "bravo", c = "charlie", d = "delta", e = "echo", f = "foxtrot")
print(phonetic)

# two ways of shallow copying dict
pcopy = phonetic.copy()
pcopy2 = dict(phonetic)

# to extend a dict use update()
phonetic.update(dict(g = "glof", h = "hotle", i = "indian")) # returns None and updates the existing dict
print(phonetic) # note the random order of dict elements 

stocks = dict(Google = 891, Apple = 123, RBS = 1.88, Facebook = 122, LinkedIn = 394)
print(stocks)
stocks.update(dict(Google = 900, RBS = 2.11)) # updates the existing keys
print(stocks)

# dict is iterable 
for k in stocks: # default iteration is used by key so this is the same as for key in stocks.keys()
    print('Company {} stock price is ${}'.format(k, stocks[k]))

# can also iterate by values; no easy way to get the corresponding keys 
for v in stocks.values():
    print(v)

#often what's used is key-value tuple pair
for k, v in stocks.items():
    print("{} => {}".format(k, v)) # one operation without extra lookup 

stocks['BAML'] = 102 # dictionary itself is mutable!
print(stocks)

# poor design of function name being the same as module name! hence must use an alias here otherwise function reference will override the module reference preventing
# access to the module.
from pprint import pprint as pp
pp(stocks) # pretty print is one of the python stand library to enable more readable form!
