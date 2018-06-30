"""Bot class module"""

#import telebot
from customTeleBot import TeleBot
import functions
import middlewares

class Bot:
    """Bot class"""
    def __init__(self, env, db):
        token = env.get("BOT_TOKEN")

        self.env = env
        self.bot = TeleBot(token)
        self.db = db

        self.functions = []
        self.middlewares = []

    def run(self):
        """run the bot"""
        self._register_actions()
        self._register_middlewares()
        self.bot.polling()

    def _discover_middlewares(self):
        for middleware in dir(middlewares):
            if str(middleware).startswith('_'):
                break
            obj = getattr(middlewares, middleware)
            self.middlewares.append(obj)

    def _discover_functions(self):
        for func in dir(functions):
            if str(func).startswith('_'):
                break
            obj = getattr(functions, func)
            self.functions.append(obj)

    def _register_middlewares(self):
        self._discover_middlewares()

        for middleware in self.middlewares:
            self.bot.add_middleware(middleware)

    def _register_actions(self):
        self._discover_functions()

        for klass in self.functions:
            routing_info = klass.info()

            trigger_info = routing_info[0]
            handler_info = routing_info[1]

            if trigger_info == "message":
                m_handler = self.bot.message_handler(**handler_info)
            elif trigger_info == "callback_query":
                m_handler = self.bot.callback_query_handler(**handler_info)
            elif trigger_info == "inline_query":
                m_handler = self.bot.inline_handler(**handler_info)
            m_handler(klass.init(env=self.env, bot=self.bot, db=self.db))