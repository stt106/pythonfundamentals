# list is a hetergeneous but mutable sequence.

# string is a list of other strings
s = "show how to index into sequences"
words = s.split() # get a list of words in the string 

 # positive index is 0 based; negative index is -1 based 
print(words[-1]) # last element of the list
print(words[-5]) # 5th element starting from the right 

# slice(startindex:stopindex)
print(words[1:4]) # note this returns a new list with [startindex, stopindex)
print(words[1:-1]) # combine slice with negative index; this excludes the first and last element
print(words)

# both start and stop index are optional; hence s[:x] + s[x:] gives the whole list  
print(words[3:]) # from 4th element to the end; 
print(words[:3]) # from the begining to the 3rd element 

# shallow copy of list; but it doesn't deep copy the elements of the list in case they mutable!
copiedWords = words[:]
print(copiedWords)
print('Is deep copy?', copiedWords is words) # show it's a shallow copy
print(copiedWords == words) # show they are value equivalent 

copiedWords[3] = 'updated!'
print(words) # unaffected! because strings are immutable!

#it's important to note that if the elements in the list are themselve mutable then modifying the shallow copy
# will affect the original list as their element still refere to the same objects. 
# other ways of shadow copying a list
copy2 = words.copy()
copy3 = list(words) # preferred way of copying as it works on copying any iterable sequence into a list  
print(copy3 == copy2)


#shallow copying of list
a = [[1, 2], [3, 4]] # nested list and note that list is mutable
b = list(a) # shallow copy of list a

print("show that it's indeed a shallow copy") 
print(a[0] is b[0]) 
print(a[0] == b[0])


a[0] = [8, 9] # this assigns the 1st element of a to a new list object; so b is unaffected!
print('b is still', b)
b[1].append(5) 
print('a now is', a) # because list is mutable; the 1st element of a is affected too!


# as in tuple, list supports repetition; it's often used to initialise a list with static length and constant value
c = [1, 2]
d = c * 3 # creates a new list with shallow copy of original list n times 
print(d)

# note that repetition is shallow copy in case the elements in the original list is mutable 
e = [[-1, 1]] 
f = e * 5
print(f)
e[0][1] = 2
print(f)


# to search element use index() which returns the index of the searching element
w = "the quick brown fox jumps over the lazy dog".split()
foxIndex = w.index("fox") # if unfound, it returns a ValueError 
print('foxindex is', foxIndex)

print('How many times does the appear?', w.count('the')) # count the element 
print('Is unicor in the it?', 'unicor' in w) # test membership; not in also works as expected 


# remove elements from the list with del element or remove(element)
del w[3] # remove the 4th element
print(w)
# del w[100] this throws IndexError.

w.remove('brown') # remove takes the actual element to be removed; if unexist will throw ValueError  
print(w)

# insert element into the list
a = "I accidentally the whole universe".split()
a.insert(2, 'destory') # insert the element into index 2 e.g. element 3
print(a)

print(' '.join(a)) # convert the list of string into a single string; only works on string list 


# different ways to grow list; these work on all iterable sequence as the input; not just list
m = [1, 2, 3]
n = [4, 5, 6]
k = m + n
print(k)
k += [7, 8, 9]
print(k)
k.extend((10, 11, 12)) # cannot omit the () for tuples here as extend only takes a single argument
print('After extending the list with a tuple', k)

# reverse and sort
k.reverse() # reverse k
print(k)
k.sort() # sort ascendingly 
print(k)
k.sort(reverse = True) # sort decendingly 
print(k)

# sort function also takes an optional parameter key which can be any callable objects which is then used to extract
# a key from each item; then list is sorted using the exacted key. 
# there are several callable objects in Python; the easiest one is function s.a. len 
h = "not perplexing do handwriting family where I illegibly know doctors".split()
h.sort(key = len) # use len function on each element and use the result as the sorting key 
print(h)

# to keep the orignal list unchanged when sorting and reverse; use reversed and sorted which work on any iterable sequence
hr = reversed(h) # h is unchanged; this returns an iterator which is lazy evaluated 
print(list(hr))
hs = sorted(h) # h is still unchanged; again returns an iterator which is evaluated only once! 
print(hs)
