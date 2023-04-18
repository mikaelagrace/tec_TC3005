from typing import Callable


# Taking a function as an argument to a function:
def add(x, y):
    return x + y


def calculate(func, x, y):
    return func(x, y)


# Returning a function from a function
def greeting(name):
    def hello():
        return "Hello, " + name + "!"

    return hello


greet = greeting("Atlantis")
print(greet())  # prints "Hello, Atlantis!"


def outer(x) -> Callable:
    def inner(y):
        return x + y

    return inner


add_five: Callable = outer(5)
result = add_five(6)
print(result)  #  what does this print?


# Function as an argument
result = calculate(add, 4, 6)
print(result)  # prints 10


# Our first decorator
def make_pretty(func: Callable) -> Callable:
    def inner():
        print("I got decorated")
        func()

    return inner


def ordinary():
    print("I am ordinary")


# decorate the ordinary function
decorated_func = make_pretty(ordinary)

# call the decorated function
decorated_func()


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()

    return inner


@make_pretty
def ordinary():
    print("I am ordinary")


ordinary()


# Examples of decorators that are actually useful


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)

    return inner


@smart_divide
def divide(a, b):
    print(a / b)


divide(2, 5)
divide(2, 0)
