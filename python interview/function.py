# basic python function syntax

def add(a,b):
    return a+b

print(add(2,3))


# function with default argument

def add(a,b=3):
    return a+b

print(add(2))


# function with variable number of arguments

def add(*args):
    return sum(args)

print(add(2,2))


# function with variable number of keyword arguments

def add(**kwargs):
    return sum(kwargs.values())

print(add(a=2,b=3,c=4,d=5,e=6,f=7,g=8,h=9,i=10))


# difference between args and kwargs
# args is tuple
# kwargs is dictionary

def add(*args, **kwargs):
    print(args)
    print(kwargs)
    return sum(args) + sum(kwargs.values())

print(add(2,3,4,5,6,7,8,9,10,a=2,b=3,c=4,d=5,e=6,f=7,g=8,h=9,i=10))




# nested function

def outer():
    def inner():
        return 'inner'
    return inner


print(outer()())

# more on nested function

def outer():
    def inner():
        return 'inner'
    return inner()

print(outer())


# lambda function

add = lambda a,b: a+b
print(add(2,3))

# higher-order function
def higher_order(func, value):
    return func(value)

def square(x):
    return x * x

print(higher_order(square, 5))

# closure
def outer_closure(x):
    def inner_closure(y):
        return x + y
    return inner_closure

closure_func = outer_closure(10)
print(closure_func(5))

# decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

