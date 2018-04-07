
class ExampleMiddleware:
    """Middleware Example"""
    def __init__(self, message):
        self.message = message

    @classmethod
    def init(cls, message):
        istance = cls(message)
        return istance.main(message)

    def main(self, message):
        # starting point:
        # param message: telebot.types.Message object
        # this function must return the message

        return message
