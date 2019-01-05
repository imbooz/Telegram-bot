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


# /broadcast command handler
def  broadcast(bot, update):
	user_ids = users.file_with_ids()
	msg_txt = update.message.text
	if update.message.from_user.id == 137786647:
		for user_id in user_ids:
			try:
				bot.send_message(chat_id=user_id, text=msg_txt[10:])
			except Exception:
				pass


broadcast_handler = CH('broadcast', broadcast)
dper.add_handler(broadcast_handler)


uper.start_polling()