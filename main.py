import logging
import users
from telegram.ext import Updater as Uper
from telegram.ext import CommandHandler as CH
from telegram.ext import MessageHandler as MH
from telegram.ext import Filters

logging.basicConfig(
	format='%(asctime)s - %(name)s - %(levelname)s - %(messages)s',
	level=logging.INFO 
	)
token = "718174216:AAG8vOUss-ku4q8fAVueYbzM_9bSoBt4e4c"
uper = Uper(token=token)
dper = uper.dispatcher


# /start command responder
def start(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="I'm a powerful bot! {}".format(update.message.chat_id))
	users.save_ids(update.message.chat_id)


start_handler = CH('start', start)
dper.add_handler(start_handler)


# /ids command responder
def ids(bot, update):
	all_ids = users.file_with_ids()
	bot.send_message(chat_id=update.message.chat_id, text="here is the list of ids: \n{}".format(all_ids))


ids_handler = CH('ids', ids)
dper.add_handler(ids_handler)


uper.start_polling()