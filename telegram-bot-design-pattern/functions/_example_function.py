"""start reply function"""

class ExampleReply(object):
    """This function reply to every new incoming message"""
    def __init__(self, env, bot, db):
        # self.env = env useless here
        self.bot = bot
        # self.db = db useless here

    @staticmethod
    def info():
        """This method returns the info for function's routing,
        the first string could be 'message', 'inline_query' or 'callback_query'.
        the second element is a dict with parameters that'll be passed through the handler
        (in our case this dict is like commands=['example',])
        """
        return ("message", {"commands": ["example",]})

    @classmethod
    def init(cls, env, bot, db):
        """This method returns the function passed to the handler
        :param env, through this param you can access the environment variables
        :param bot is an istance of the Bot class
        :param db is an istance of the database's connection
        """
        istance = cls(env, bot, db)
        return istance.main

    def main(self, message):
        """This is the function's starting point.
        :param message, it's the incoming message object
        """
        self.bot.reply_to(message, "It works!")
