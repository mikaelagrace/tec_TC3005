"""Adapted from :https://medium.com/design-patterns-in-python/observer-pattern-c58820ad3c9f

Which is a great explanation of the pattern.

"""

from abc import ABCMeta, abstractmethod


class PublisherInterface(metaclass=ABCMeta):
    """This class represents The Publisher/Subject Interface"""

    @staticmethod
    @abstractmethod
    def subscribe(observer):
        pass

    @staticmethod
    @abstractmethod
    def unsubscribe(observer):
        pass

    @staticmethod
    @abstractmethod
    def notify(observer):
        pass


class Publisher(PublisherInterface):
    """This class represents Concrete Subject/Publisher"""
    raise NotImplementedError("TODO implement!")


class SubscriberInterface(metaclass=ABCMeta):
    """This is an interface for the Observer/Subscriber"""

    @staticmethod
    @abstractmethod
    def notify(observable, *args):
        pass


class Subscriber(SubscriberInterface):
    """This is a Concrete Observer/Subscriber"""

    def __init__(self, observable):
        observable.subscribe(self)

    def notify(self, observable, *args):
        print(f"Observable is: {observable}")
        print(f"Observer id:{id(self)} received {args}")


if __name__ == '__main__':
    # The Client Code
    publisher = Publisher()
    subscriber_a = Subscriber(publisher)
    subscriber_b = Subscriber(publisher)
    publisher.notify("First Notification", [1, 2, 3])
    publisher.unsubscribe(subscriber_b)
    publisher.notify("Second Notification", {"A": 1, "B": 2, "C": 3})
