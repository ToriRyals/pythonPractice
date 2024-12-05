print('e')
name = input('What year were you born? ')  # takes as a str
print(type(name))
# Different Data Types:
# 1. Fundamental Data types - int, float, complex (real numbers), bool, str, list, tuple, set, dict
print(type(2 / 4))
print(2 ** 2)  # 2 to the power of 2
print(5 // 4)  # gets rounded to an integer
print(6 % 4)  # modulo
print(round(3.1))  # rounds
print(abs(-20))
print(bin(5))
print(int('0b101', 2))
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

# Operator precedence - (), **, * /, + -
# Variables - snake_case, start with lowercase, case-sensitive, no keywords
# __dunder variables start with two __
# Augmented operators +=, -=. *= etc

# Strings- ' ', " ", ''' ''' (long string), string concatenation
print(type("hello"))
print(len("hello"))
long_string = '''
WOW
0 0
---
'''
print(long_string)
print(type(int(str(100))))  # type conversion
print("\tIt\'s \"kind of\" sunny \n hope you have a good day")  # escape sequences
name = "Johnny"
age = 55
print(f'hi {name}. You are {age} years old')  # 3.0
# 2.0 uses .format instead of f

# String indexes/slicing - [start:stop:stepover]
selfish = '01234567'
print(selfish[0:8:2])
print(selfish[1:])
print(selfish[:5])
print(selfish[::1])
print(selfish[-1])
print(selfish[::-1])  # reverse a string
print(selfish[0:len(selfish)])

password = 'secret'
hidden_password = '*' * len(password)
print(hidden_password)

# strings are IMMUTABLE, cant reassign part of a string, have to create something new
# strings have built in methods, ie - .upper(), .capitalize(), .find(), .replace()

# Lists are like arrays, a collection of items and basic data structure, and can be sliced
# also have built in methods that work in place like:
# Adding: .append() (changes original list), .insert(index, value), .extend()
# Removing: .pop(index), .remove(value), .clear()
# Index: .index(value, start, stop), in (returns a bool if exists), .count(value)
# Sort: .sort() (sorts in place), sorted() (produces new array)
# Copy: .copy()
# Reverse: .reverse() reverse in place
# Range: range(start, stop)
# Join: string.join() adds list into a string
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]
print(amazon_cart[0::2])
amazon_cart[0] = 'laptop'
print(amazon_cart)
# list slicing creates a copy, doesn't modify the original list unless you reassign
new_cart = amazon_cart
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

# List Unpacking
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(*other)
print(d)

# Matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])

# Dictionary, has an unordered key, value dichotomy
dictionary = [{
    'a': [1, 2, 3],
    'b': 2,
    'c': True,
    'd': 'hello'
},
    {
        'a': [1, 2, 3],
        'b': 2,
        'c': True,
        'd': 'hello'
    }]
print(dictionary[0]['a'][2])

# List is sorted, dictionary isn't and hold more info
# Keys have to be immutable and has to be unique
# Methods:
# .get(key, default value)
# dict(key=value) creates dict
# in: variable in dict.values(), dict.keys()
# items: dict.items() returns pairs of key,values as tuples
# .clear()
# .copy()
# .pop(key) returns value and removes pair
# .popitem() returns value and removes last pair
# .update({key: value})

# Tuple - immutable lists and can be sliced
# .count()
# .index()
my_tuple = (1, 2, 3, 4, 5)

# Set-unordered collections of unique objects with built-in functions
my_set = {1, 2, 3, 4, 5, 5}
print(my_set)
# set(list) removes duplicates and creates a set from a list
# cant use indexing because its unordered, use in instead to grab by item
# .copy()
# .clear()

my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

print(my_set.difference(your_set))
my_set.discard(5)
print(my_set)

my_set.difference_update(your_set)
print(my_set)

print(my_set.intersection(your_set))  # print(my_set & your_set) works as well

print(my_set.isdisjoint(your_set))

print(my_set.union(your_set))  # print(my_set | your_set) works as well

print(my_set.issubset(your_set))
print(my_set.issuperset(your_set))
print(your_set.issuperset(my_set))

# 2. Classes -> custom types
# 3. Specialized Data Types, ie Modules
# 4. None - like 0
# Like null
weapons = None
print(weapons)
