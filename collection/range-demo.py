# default start value is 0; stop value for range is one past the end
for i in range(5):
    print(i) # stops at 4!

for i in range(5, 10): # [5, 10)
    print(i) 

for i in range(10, 20, 2): # optional 3rd step value
    print(i)

# never use range with len to create an indexer because python support itertable so use for...in directly. 
# enumerate() yields (index,value) tuples
t = [323, 452, 694, 19485]
for i, v in enumerate(t):
    print("i = {}, v = {}".format(i, v)) # use tuple unpacking returned by enumerate()
