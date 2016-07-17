# string of type str; "" and '' are both ok but be consistent 
print("hello" " world") # adjacent strings are concatenated together into a single string 

# multiple line string using """ or ''' 
print("""this is a 
... multiple lines string""")

print('''this is another
... multiple line string''')

print('this is using\n new line operator\n due to python''s universal new line support in python 3')

# backslash also escapes ', " and backslash
print('this is a\'')
print("this is a \"")
print('this is a \\')

# a raw string is helpful in file paths
path = r'C:\TestFolder'
print(path)

# conver to strings
print(str(4.34))
print(str(4.4e4))

## Note that there is no character type like other languages; each element of a string is simply another string
someString = "some string"
print(type(someString[3])) # class str 

# like other languages, strings are immutable
c = 'london'
print(c.capitalize())
print(c)



### collections

# list are dynamically types and it's mutable
l1 = [1, 2, 'hello']
print(l1)
l1.append(3)
print(l1)
l2 = list('characters') # list ctor; creates a list of strings
print(l2)

# dictionary is mutable mapping of key and value 
contracts = {'mandy' : '07741', 'rita' : '06777'}
contracts['ben'] = '49299' # a new item is added 

# putting it all together
from urllib.request import urlopen
with urlopen('http://sixty-north.com/c/t.txt') as story:
    words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            words.append(word)
print(words)

