from typing import Callable


def star(func: Callable) -> Callable:
    """A decorator that prints 15 * before and after the function call"""
    # TODO(students): implement this function
    pass


def reverse_first_arg_string(func: Callable) -> Callable:
    """A decorator that reverses the first argument of the function call"""
    # TODO(students): implement this function
    pass


@star
@reverse_first_arg_string
def printer(msg1, msg2, msg3):
    print(msg1)
    print(msg2)
    print(msg3)


if __name__ == '__main__':
    printer("i love python", "1234", "abcd")
"""
Desired Behavior:

INPUT:
printer("i love python", "1234", "abcd")

OUTPUT:
***************
nohtyp evol i
1234
abcd
***************

"""
