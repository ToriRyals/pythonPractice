#functions are first class citizens and can be passed around like variables (as parameters in other functions)
#@decorator adds functionality

#Higher Order Function - function that accepts another function as a parameter
def hello2(func):
    func()

def greet2():
    def func():
        return 5
    return func

def greet():
    print("still here")

print(greet())
a = hello2(greet)
print(a)



def my_decorator(func):
    def wrap_func():
        print("*******")
        func()
        print("*******")
    return wrap_func

@my_decorator
def hi():
    print("hellooooo")

@my_decorator
def bye():
    print("byeeee")


hi()
bye()
#hello2 = my_decorator(hello)
#hello2() -- is the same thing as the @

#or even my_decorator(hello)()


#Decorator Pattern
def my_decor(func):
    def wrap_funct(*args, **kwargs):
        func(*args, **kwargs)
    return wrap_funct

@my_decor
def hey(greeting, emoji=":)"):
    print(greeting, emoji)

hey("hiii")

from time import time
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper

@performance
def long_time():
    for i in range(10000):
        i*5

long_time()
