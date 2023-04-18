"""Note: This is a simple, somewhat-contrived example of the MVC pattern.

Usually, for something this simple, you wouldn't need to implement this pattern.

The purpose of this example is to show how the pattern works, and to show how to
implement it in Python."""
from model import QuoteModel
from view import QuoteTerminalView


class QuoteTerminalController:
    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteTerminalView()

    def run(self):
        valid_input = False
        quote = None
        while not valid_input:
            try:
                n = self.view.select_quote()
                n = int(n)
                quote = self.model.get_quote(n)
                valid_input = True
            except Exception as e:
                self.view.error(f"Incorrect index '{n}'")
        self.view.show(quote)


if __name__ == "__main__":
    controller = QuoteTerminalController()
    while True:
        controller.run()
