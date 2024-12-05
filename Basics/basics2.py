is_old = True
is_licensed = True
if is_old and is_licensed:
    print("you old!")
elif is_licensed:
    print("you can drive")
else:
    print("YOUNG")

# Truthy and Falsey
print(bool(""))
print(bool(0))
print(bool(5))
print(bool("hello"))

# Ternary Operator/Conditional Expression
# condition_if_true if condition else condition_if_false
is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"

# Short Circuiting
is_user = True
if is_friend or is_user:
    print("bff")

# Logical Operators: and, is, or, not, >, <, ==, <=, >=, !=
# is checks if the location in memory is the same, like == in java, == checks for value in python

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}
# For loops
for item in (1, 2, 3, 4, 5):
    for x in ['a', 'b', 'c', 'd']:
        print(item, x)

# Iterables - list, dictionary, tuple, set, string (a collection of items)
for k, v in user.items():
    print(k, v)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

# range(stop) - special object gives you a range that can be iterated over, can also use range(start, stop, stepover)
for number in range(5):
    print(number)
for _ in range(10, 0, -1):  # go in reverse
    print(_)
for _ in range(2):
    print(list(range(10)))

# enumerate - gives an index counter for an item
for i, char in enumerate(list(range(5))):
    print(i, char)
    if char == 3:
        print(f"index of 3 is: {i}")

# while - else executes when done with while loop
# if you know how many times you want to iterate use a for, when you dont know how many times use a while
# break, continue, pass (passes to the next line)
i = 0
while i < 5:
    print(i)
    i += 1
    break  # skips else
else:
    print("all done")

my_list = [1, 2, 3]
for item in my_list:
    # thinking about it
    pass


# Functions - def, can nest functions, but need to use return or else returns None
# default parameters
def say_hello(name="Darth Vader", emoji="XD"):
    print(f"hello {name} {emoji}")
    return 5


# positional arguments
say_hello("Tori", ":)")
say_hello(name="Tori", emoji=':)')  # bad practice to do keyword arguments
say_hello()
print(say_hello())


# Docstrings
def test(a):
    '''
  Info: this function tests and prints param a
  '''
    print(a)

test("sdfasdf")
help(test)
print(test.__doc__)


# *args- accepts any number of positional arguments
# **kwargs - keyword args turns keyword arguments into a dictionary
# Rule: params, *args, default parameters, **kwargs
def super_func(name, *args, i="hi", **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func("Andy", 1, 2, 3, 4, 5, num1=5, num2=10))

# walrus operator := assigns a variable in the middle of expressions
a = "helloo"
if (n := len(a)) > 4:
    print(f"too long {n} elements")

while (n := len(a)) > 1:
    print(n)
    a = a[:-1]

print("Scope priority: local, parent local, global, built in python functions")
total = 0
def count():
    global total
    total += 1
    return total

count()
count()
print(count()) #not a great practice to use global because of dependencies

#better:
def count(total):
    total += 1
    return total
print(count(count(count(total))))

#nonlocal - used to refer to not global but parent variable, not a great practice because it makes code unpredictable

