import datetime

from SingletonByArgs import SingletonByArgs
from factorization import gnu_factor

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


MAX_INPUT_SIZE = 1000 # 1Kb of text

def start(update, context):
    update.message.reply_text('Hello, type some numbers to factor them.')

def help(update, context):
    update.message.reply_text('Type numbers to factor them. Any not valid number will be ignored, ex: 123dz')    

def reply(update, context):
    input = update.message.text
    print(input)
    if len(input) > MAX_INPUT_SIZE:
        update.message.reply_text('Input size is to big. Please, send message with 1000 or less characters.')
    else:
        try:
            output = gnu_factor(input)
            update.message.reply_text(output)
        except Exception as e:
            print (e)
        

class FactorNumbersBot(metaclass=SingletonByArgs):
    def __init__(self, bot_api_key):
        self.updater = Updater(bot_api_key, use_context=True)
        dp = self.updater.dispatcher

        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))

        dp.add_handler(MessageHandler(Filters.text, reply))

    def start(self):
        print(self.updater)
        return self.updater.start_polling(poll_interval=0.12)

    def stop(self):
        self.updater.stop()


def main():
    pass

if __name__ == '__main__':
    main()
