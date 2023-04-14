from abc import abstractmethod


class Animal:
    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        print("meow")


class Dog(Animal):
    def make_sound(self):
        print("woof")
