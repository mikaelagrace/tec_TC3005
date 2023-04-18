class MyMeta(type):
    """
    Delegates via super() to the __new__() method of the parent metaclass (type) to actually create a new class
    Assigns the custom attribute attr to the class, with a value of 100
    Returns the newly created class
    """

    def __new__(cls, name, bases, dct):
        new_instance = object.__new__(cls)
        new_instance.attr = 100
        return new_instance


class MyClass(metaclass=MyMeta):
    pass


class MySubclass(MyClass):
    pass
