from telegram.ext import Updater, CommandHandler
from config import BOT
import requests

def start(update, context):
    print(update.effective_chat.id)
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a zed notification board.")


class ZedNotification:

    instance = None

    @classmethod
    def get_instance(cls):
        if not ZedNotification.instance:
            ZedNotification.instance = cls()
        return ZedNotification.instance

    def __init__(self): 
        self.updater = Updater(token=BOT.get('token'),use_context=True)
        self.dispatcher = self.updater.dispatcher 
        start_handler = CommandHandler('start', start)
        self.dispatcher.add_handler(start_handler)

    def run(self):
        self.updater.start_polling()

    def send_message(self, message):
        token = BOT.get('token')
        channel = BOT.get('channel')
        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={channel}&text={message}"
        response = requests.get(url)


Notification = ZedNotification.get_instance()
