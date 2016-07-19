# comprehensions and for loop are the most common way to iterate the whole sequenec by default. But sometimes some fine-grained control is needed.
# Iterable protocol: iter() which takes an iterable object such as string or list and returns an iterator.
# Iterator protocol: next() which takes an iterator objects to fetch the next item. 
# Note that comprehension and for loop are built upon iterator and iterable protocols. 

iterable = ["Spring", "Summer", "Autumn", "Winter"]
iterator = iter(iterable) # return an iterator
print(next(iterator)) # next() will start iterating through the iterable objects
print(next(iterator))
print(next(iterator))
print(next(iterator))
try:
    print(next(iterator)) # raise StopIteration exception
except StopIteration:
    print('Reached the end of iterable object!') 

# Generator functions provide the means for describing iterable series with code and functions. e.g. all generators are iterators
# The series is lazily evaluated; e.g. only compute on demand.
# Can model infinite sequences and can be composed together into pipelines. 

# define a generator function
def gen123():
    yield 1
    yield 2
    yield 3

g = gen123() # this hasn't executed anything as it's lazily evaluated
print(next(g))
print(next(g))

# because generators are iterators they can be used in for loop
for i in gen123():
    print(i)

# each generator function call returns an independent generator 
h = gen123()
g = gen123()
print(h is g) # two references refer to two different objects!
print(h == g)

# each generator can be looped independently
next(h)
next(h)
print(next(g)) # return 1 as it's independent of h 


# stateful generator functions
def take(count, iterable):
    """Take items from the front of an iterable.
    
    Args:
        count: The maximum number of items to retrieve.
        iterable: The source series.

    Yields:
        At most 'count' items from 'iterable'
    """
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def distinct(iterable):
    """Return unique items by eliminating duplicates.
    
    Args:
        iterable: The source series.

    Yields:
        Unique elements in order from 'iterable'
    """

    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item) # generator remembes the state after yielding result before the next yield!


def run_take():
    numbers = [3, 4, 569, 1, 4, 596, 67]
    takeThree = take(3, numbers)
    for t in takeThree:
        print(t)


def run_distinct():
    numbers = [4, 59, 18, 48, 128, 58]
    dist = distinct(numbers)
    for d in dist:
        print(d)


def main():
    run_distinct()



# generator comprehensions using tuple form!

hunderd_square = (x*x for x in range(100)) # lazily evaluated so no square has been computed yet
print(sum(hunderd_square)) #

# this gives 0 because once a generator object is exhaustive it will yield no more items hence returns empty collection.
# generator objects are single-use objects; each time a generator function is called it creates a generator object!
print(sum(hunderd_square))  

# calculate a large sum using little memory due to it lazy evaluation e.g. doesn't have to hold all the squares in memory at the same time!
largeSum = sum(x*x for x in range(1, 1000001)) # sum of first 1M squares; when passing a generator expression into a function the () for generator itself is optional!

#iteratortool module provides more built-in generator functions to aid powerful functional programming!

if __name__ == '__main__':
    main()