# Comprehensions in python are a concise syntax for describing lists, sets or dictionaries in a declarative or functional style. 
# This shorthand is very readable and expressive hence greatly improves communications. 

# list comprehensions
words = "Why sometimes I have believed as many as six impossible things before breakfast".split()

# general form of comprehension is [expr(item) for item in iterable]
words_length = [len(word) for word in words] # create a new list using comprehensions
print(words_length)


from math import factorial
flength = [len(str(factorial(i))) for i in range(20)]
print(flength)


# set comprehensions
unique_length = {len(str(factorial(i))) for i in range(20)}
print(unique_length)


#dictionary comprehensions
country_to_capital = {'UK' : 'London', 'Brazil' : 'Brazilia', 'Morocco' : 'Rabat', 'Sweden' : 'Stockholm'}
# creat a new dict using capital as key and country as the value 
capital_to_country = {
                        capital : country for country, capital # using tuple unpacking to access key and value 
                                          in country_to_capital.items() # using dict.items() to iterate both key and value 
                     }
print(capital_to_country)

# in dictionary comprenehsions if duplicate keys exist; the later value will override the earlier value
words = {'hi', 'hello', 'foxtrot', 'hotel'}
d = {x[0] : x for x in words} # only hotel is returned as the h key overrides the previous two values 
print(d)                     

# list, set and dict comprehensions can take a filter predicate to filter out result before returning to the comprehensions
odd_squares = {x : x * x for x in range(20) if x % 2 != 0}
print(odd_squares)

