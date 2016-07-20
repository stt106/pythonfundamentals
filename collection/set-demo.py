# set is an unordered collection of unique, hetergeneous and immutable objects (everything is an object in python); 
# that is the set itself is mutable but each element must be immutable (like the key in dict) 

#consturction
s1 = {3, 423, 54, 289, 862, 485, '3', 3} # unique immutable objects as elements and it's unordered! dupliates are ignored!
print(s1)
sempty = set() # cannot use {} as it creates an empty dict 
print(type(sempty))

# a common usage of set is removing duplicates!
s2 = set([1,2, 3, 2, 3, 4]) # convert list to set removing any duplicates;
print(s2) 

s3 = set((1, 2, 3, 2)) # convert tuple into set 
print(s3)

# of course set is iterable
for i in s1:
    print(i) # the order is random!!!

# membership test using in and not in just like any other iterable sequence 
print(3 in s1)

# add a single element to set
s1.add(100)
print(s1)
s1.add(100) # adding duplicates is ignored!
print(s1)

# add multiple elements from another sequence or set; again duplicates are ignored!
s1.update([200, 300])
print(s1)
s1.update({100, 400, 500})
print(s1)

# two ways to remove elements from the set
s1.remove(100) # removing 100 and 100 must exist in the set
#s1.remove(100) # this throws an error 
s1.discard(100) # this is less fussy if 100 is not in the set 

# like other collections; copy is a shallow copy i.e. copying the reference but not the object it refers to
scopy = s1.copy()
print(scopy is s1)

# set algebra; 
# union (combine two sets);
# intersect (common of two sets);
# difference (elements in the first set but not the second set )
# symmetric (elements in only one of the set but not both)
# s.issubset(anotherset) (whether the 2nd set is a subset of the first set)
# issuperset (tests whether set 1 is a super set of set 2)
# isdisjoint (test whether two sets have nothing in common; e.g. interestion is empty!)

# in Python, a protocol is a set of operations that must be supported by the type; they're like interfaces in C#
# Protocl Name                                                                       Implementing Collections
# Container (membership test using in or not in)                                    str, list, range, tuple, dict, set bytes
# Sized (determine number of elements with len(s))                                  str, list, range, tuple, dict, set bytes
# Iterable (yield element one by one that can be used in for loop)                  str, list, range, tuple, dict, set bytes
# Sequence (retrieve elements by index e.g. seq[index],                             str, list, range, tuple, dict, set bytes 
#   find item by value e.g. seq.index(item), 
#   count items e.g. seq.count(item), 
#   produce a reversed and sorted sequence e.g. reversed(seq))       
# Mutable Sequence                                                                  list
# Mutable set                                                                       set
# Mutable mapping                                                                   dict                                               

