
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

        print("Message %(msg_text)s seen by the %(class_name)s middleware!" % ({ 
            'msg_text': message.text,
            'class_name': self.__class__.__name__
            }))

        return message
