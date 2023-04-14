class Car:
    wheels = 4  # <- Class variable

    def __init__(self, color):
        self.color = color  # <- Instance variable

    def print_color(self):
        print(self.color)

    @classmethod
    def print_wheels(cls):
        print(cls.wheels)

    @staticmethod
    def say_hi():
        print("Hi")


def methods_example():
    car1 = Car("red")
    car1.print_wheels()
    Car.print_color()
    car1.say_hi()
    Car.say_hi()


def variables_example():
    car1 = Car("red")
    car2 = Car("blue")
    print(car1.color)
    print(car2.color)
    print(car1.wheels)
    print(car2.wheels)

    Car.wheels = 3
    print(car1.wheels)
    print(car2.wheels)
    car1.wheels = 6

    print("after setting car1.wheels to 6")
    print(car1.wheels)
    print(car2.wheels)
