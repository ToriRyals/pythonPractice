#iterable - any object in python were able to loop through
#iterate - doing something with an iterable
#generators are iterables, a range is a generator because it is an iterable, but a list is an iterable but not an iterator
#generators are a subset of iterables and are useful for processing large amounts of data
range(100)
list(range(100))

def generator_function(num):
    for i in range(num):
        yield i*2 #keeps track of state

g = generator_function(100)
next(g)
next(g)
print(next(g))


def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b

def fib2(number):
    a = 0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result


# for x in fib(100):
#     print(x)
print(fib2(10))