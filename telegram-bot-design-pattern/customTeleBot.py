import telebot

class TeleBot(telebot.TeleBot):
    """custom TeleBot Class"""

    # adding new class variable that stores middlewares' classes
    middlewares = []

    # adding a function that appends new middlewares
    def add_middleware(self, middleware):
        self.middlewares.append(middleware)

    ## OVERRIDE ##

    def _notify_command_handlers(self, handlers, new_messages):
        for message in new_messages:

            # first, every message is processed by all the middlewares
            for middleware in self.middlewares:
                message = middleware.init(message)

            # if message has next step handler, dont exec command handlers
            if hasattr(message, 'chat') and message.chat and (message.chat.id in self.message_subscribers_next_step):
                continue
            for message_handler in handlers:
                if self._test_message_handler(message_handler, message):
                    self._exec_task(message_handler['function'], message)
                    break
