# Telegram Bot design pattern

Are you interested in a cleam telegram bot' structure? This pattern allows you to organize all your function, db connections, models, env files in a pretty and organised way.

This pattern uses the fabolous [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI]) library as its message handler.

## Prerequisites

You need **pyTelegramBotAPI**, **python-dotenv** installed on your computer, as specified in the [requirements.txt](requirements.txt) file.

## Installation

Clone this repository:

```shell
git clone https://github.com/lucaoflaif/telegram-bot-design-pattern
```

Then install the necessary dependencies using **pip** command-line tool:

```shell
cd telegram-bot-design-pattern
[sudo] pip install -r requirements.txt
```

And copy the `.env.sample` file to `.env` to fill it with the needed data:

```shell
cp .env.sample .env
```

Start our bot with:

```shell
python main.py
```

## Documentation

Let's see the structure.

### Functions

Obviously, the pattern will handle the Bot function's, simply, all your functions must be saved in the [functions](functions/) folder, each function will be a class in a python file that **must start with one or more underscore symbol**. Let's the [Example function file](functions/_example_function.py).

```python
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
    def init(cls, env, bot, market):
        """This method returns the function passed to the handler
        :param env, through this param you can access the environment variables
        :param bot is an istance of the Bot class
        """
        istance = cls(env, bot, market)
        return istance.main

    def main(self, message):
        """This is the function's starting point.
        :param message, it's the incoming message object
        """
        self.bot.reply_to(message, "It works!")

```

as you can see the code is well commented:

-**`__init__()`**: to the constructor function the core mechanism will pass:
| env | bot | db  |
|:---|:---:|---:|
|The object thanks to wich you'll be able to access your .env file|  The Telegram Bot object instance (See the pyTelegramBotAPI doc's ['TeleBot'](https://github.com/eternnoir/pyTelegramBotAPI#telebot) section)  |  Te object that will allow you to use your database connection object  |

-**info()**: here you can specify all the info allowing the Bot instance to handle your message. I.E. the statement:

```python
return ("message", {"commands": ["example",]})
```

let the bot trigger the current function through the `/example` command, in fact it's perfectly equals to

```python
@bot.message_handler(commands=['example',])
```

See the pyTelegramBotAPI doc's ['a simple echo bot'](https://github.com/eternnoir/pyTelegramBotAPI#a-simple-echo-bot) section.

-**init()**: nothing to see or modify here, it returns to the core mechanism the main function.

-**main()**: your function's logic lies here, you can access the Bot methods through the `self.bot` local variable, and the incoming [message object](https://github.com/eternnoir/pyTelegramBotAPI/blob/9ae20b48154fe39aa92049fdb2336f6246aaa13f/telebot/types.py#L251) through the message param.

### Middlewares

"Okay, now, for every message, I'd want to display the text of the message in my terminal, how can I implement this in my function?"

Simply, don't, God gave us Middlewares. A middleware is executed before **every** message. Let's see a middleware structure opening the [middlewares/_example_middleware.py](middlewares/_example_middleware.py) file. (Like functions, **every middleware file must start with one or more underscore symbol**.)

```python
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
```

-**__init__**: we initialize our message object as a class variable.

-**init()**: nothing to see here, this method return our middleware to the core mechanism.

-**main()**: your middleware's logic lies here. **the main method must always return the message object**

So now, if we want to display, for each request, the text of the message, our middleware will simply contain:

```python
    ...
    def main(self, message):
        # starting point:
        # param message: telebot.types.Message object
        # this function must return the message

        print (message.text)

        return message
```

The message text will be printed and then the core mechanism will pass the message object to all the other middlewares first, and to the functions then.
Let's do something 

## Authors

CryptoTrackerBot is mantained by Luca Di Vita - [GitHub](https://github.com/lucaoflaif) - [Telegram](www.google.it)

## License

**telegram-bot-design-pattern** is released under [MIT license](LICENSE).