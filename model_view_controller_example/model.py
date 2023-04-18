"""Note: This is a simple, somewhat-contrived example of the MVC pattern.

Usually, for something this simple, you wouldn't need to implement this pattern.

The purpose of this example is to show how the pattern works, and to show how to
implement it in Python."""

from fake_database import quotes


class QuoteModel:
    def get_quote(self, n):
        try:
            value = quotes[n]
            return value
        except IndexError as err:
            raise ValueError("Invalid quote number: {}".format(n)) from err
