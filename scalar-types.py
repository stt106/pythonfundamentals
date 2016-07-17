# integer by default by specified by decimals but other forms are also available
print('decimal form: ' + str(10))  # with base 10
print('binary form: ' + str(0b10)) # with base 2 
print('Octal form: ' + str(0o10))  # with base 8
print('hex form: ' + str(0x10))    # with base 16

# convert to int using int ctor
print(int(3.4))
print(int(-3.9))
print(int("4924")) # default base is 10
print(int("1000", 2)) # passing 2 as the base 

# convert to float 
print(3 + 4.0) # int and float result float 
print(float("3.45"))
print(2.34e4)
print("inf") # +infinity
print('-inf') # -infinity
print('nan') # nan is a float number

# special type None which has sole value None often representing abstance of value and it's not evlauted by the REPL
a = None
print(a is None) # test equality

# boolean type: 0 (0.0), empty string, None and empty collection are falsy
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool([]))
print(bool(None)) # flase 

# all other numbers and non-empty string and collections are truey, including the string 'False'
print(bool('False'))
print(bool(1.2))
print(bool(-3))
print(bool([1,2,3]))

# there is a shortcut to convert other types to boolean in conditional statement
if "eggs": # bool ctor is rarely used in python  
    print("sounds nice!")   

# Flat is better than nested so use elif when possible to avoid nesting if under else block

# break terminates the innermost loop
       