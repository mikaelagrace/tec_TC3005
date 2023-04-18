"""Adapted from :https://medium.com/design-patterns-in-python/observer-pattern-c58820ad3c9f

Which is a great explanation of the pattern.

"""

from abc import ABCMeta, abstractmethod


class PublisherInterface(metaclass=ABCMeta):
    """This class represents The Publisher/Subject Interface

    A class that has a metaclass derived from ABCMeta cannot be instantiated unless all
     of its abstract methods and properties are overridden

    """

    @staticmethod
    @abstractmethod
    def subscribe(subscriber):
        pass

    @staticmethod
    @abstractmethod
    def unsubscribe(subscriber):
        pass

    @staticmethod
    @abstractmethod
    def notify(subscriber):
        pass


class Publisher(PublisherInterface):
    """This class represents Concrete Subject/Publisher"""

    def __init__(self):
        self._subscriber = set()

    def subscribe(self, subscriber):
        self._subscriber.add(subscriber)

    def unsubscribe(self, subscriber):
        self._subscriber.remove(subscriber)

    def notify(self, *args):
        for subscriber in self._subscriber:
            subscriber.notify(self, *args)


class SubscriberInterface(metaclass=ABCMeta):
    """This is an interface for the Observer/Subscriber"""

    @staticmethod
    @abstractmethod
    def notify(publisher, *args):
        pass


class Subscriber(SubscriberInterface):
    """This is a Concrete Observer/Subscriber"""

    def notify(self, publisher, *args):
        print(f"Observable (publisher) is: {publisher}")
        print(f"Observer (subscriber) id:{id(self)} received {args}")


if __name__ == "__main__":
    # The Client Code
    publisher = Publisher()
    subscriber_a = Subscriber()
    subscriber_b = Subscriber()
    publisher.subscribe(subscriber_a)
    publisher.subscribe(subscriber_b)
    publisher.notify("First Notification", [1, 2, 3])  # TWO SUBSCRIBERS GET NOTIFIED
    publisher.unsubscribe(subscriber_b)
    publisher.notify(
        "Second Notification", {"A": 1, "B": 2, "C": 3}
    )  # ONE SUBSCRIBER GETS NOTIFIED
