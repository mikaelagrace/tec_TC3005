from typing import List, Dict, Callable, Tuple, Set

def my_func(a, b):
    return a + b

my_func(a=1, b=2)

# ARGS
def adder(*args):
    sum = 0
    print('type of num parameter: {}'.format(type(args)))
    for n in args:
        sum = sum + n

    print("Sum:", sum)


# KWARGS
def kwargs_example(**kwargs):
    print("type of kwargs parameter: {}".format(type(kwargs)))

    for key, value in kwargs.items():
        print("{} is {}".format(key, value))


if __name__ == '__main__':
    #adder(3, 5)
    #adder(4, 5, 6, 7)
    #adder(1, 2, 3, 4, 5, 6, 7, 8, 9)
    kwargs_example(name="Jane", age=36)
    kwargs_example(my_name="Jane", age=36, address="123 Main St")
    kwargs_example(name="Jane", age=36, address="123 Main St", phone="555-555-5555")
