# --------------------------
# -- DATA TYPES --
# --------------------------
# [type()] obtain data type
# [str] String
# [123] Number
# [True/False] Boolean
# --------------------------

# aiteral assignment
import math
first = 'yuan'
last = 'wu'

# print(type(first))  # <class 'str'>
# print(type(first) == str)  # True
# print(isinstance(first, str))
# True: isinstance compares the 'first' to if it is a string data type


# constructor function
pizza = str('Pepperoni')

# print(type(pizza))  # <class 'str'>
# print(type(pizza) == str)  # True
# print(isinstance(pizza, str)) # True


# concatenation
fullname = first + " " + last
# print(fullname)  # yuan wu

fullname += '!'
# print(fullname)  # yuan wu!

# casting a num to ba str
decade = str(1980)
# print(type(decade))
# print(decade)

statement = 'I like rock music from the ' + decade + 's.'
# print(statement)  # I like rock music from the 1980s.

# multiple lines
multiline = '''
Hey, How are you?

I was just checking in.   
                            All good?

'''
# print(multiline)


# escaping special char.
# [\] Esc a special char.
# [\t] Tab
# [\n] New line

sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at \\located?'
# print(sentence)


# --------------------------
# ----- String Methods -----
# --------------------------
# [.lower()] To lowercase
# [.upper()] To uppercase
# [.title()] To title case, where the 1st char is uppercased
# [.replace("og_val", "new_val")] Replaced from val_1 to val_2
# [.len()] Lenght of sth
# [.stripe()] To strip away the empty spaces
# [.lstripe()] To remove empty spaces from the LEFT
# [.rstripe()] To remove empty spaces from the RIGHT
# [.center(char. length, "some symble/special char.")] To center sth
# [.ljust(length,'sperator/filler char')]
# [.rjust()]
# --------------------------


# build a menu
title = 'menu'.upper()
print(title.center(20, '-'))
print('Coffee '.ljust(17, '.') + '$1'.rjust(3))
print('Muffin '.ljust(17, '.') + '$2'.rjust(3))
print('Cheesecake '.ljust(17, '.') + '$4'.rjust(3))

print('')

# string index values
print(first[1])  # u
print(first[-1])  # n
print(first[1:-1])  # ua: start from ind. 1 and omit the last(-1) char.
print(first[1:])  # uan: start from ind. 1 and incl. the last char

# some methods return boolean data
print(first.startswith('Y'))
print(first.endswith("o"))

fname = first.lower()
print(fname.startswith('y'))

print('\n')

# Boolean data type
myval = True
x = bool(False)
print(type(x))  # <class 'bool'>
print(isinstance(myval, bool))  # True

print('\n')

# integer type
price = 100
best_price = int(80)
print(type(price))  # <class 'int'>
print(isinstance(best_price, int))  # True


# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))  # <class 'float'>


# complex type
comp_val = 5+3j
print(type(comp_val))  # <class 'complex'>
print(comp_val.real)  # 5.0
print(comp_val.imag)  # 3.0


# build-in fn for numbers
print(abs(gpa))  # 3.28
print(abs(gpa * -1))  # 3.28
print(round(gpa))  # 3
print(round(gpa, 1))  # 3.3

print(math.pi)  # val of pi
print(math.sqrt(64))  # 8
print(math.ceil(gpa))  # 4
print(math.floor(gpa))  # 3


# casting a str to a num
zipcode = '11421'
zip_val = int(zipcode)
print(type(zipcode))
print(zip_val)

# error if attempt to cast incorrect data
# zip_val = int('New York')
