"""Note: This is a simple, somewhat-contrived example of the MVC pattern.

Usually, for something this simple, you wouldn't need to implement this pattern.

The purpose of this example is to show how the pattern works, and to show how to
implement it in Python."""


class QuoteTerminalView:
    def show(self, quote):
        print(f'And the quote is: "{quote}"')

    def error(self, msg):
        print(f"Error: {msg}")

    def select_quote(self):
        return input("Which quote number would you like to see? ")
