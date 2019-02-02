import logging
import users
from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater as Uper
from telegram.ext import CommandHandler as CH
from telegram.ext import MessageHandler as MH
from telegram.ext import CallbackQueryHandler as CQH
from telegram.ext import Filters

logging.basicConfig(
	format='%(asctime)s - %(name)s - %(levelname)s - %(messages)s',
	level=logging.INFO 
	)
token = "718174216:AAG8vOUss-ku4q8fAVueYbzM_9bSoBt4e4c"
uper = Uper(token=token)
dper = uper.dispatcher


global current_position
current_position = "Nothing"

print(current_position)

# /start command responder
def start(bot, update):
	keyboard = [
				[
				 KeyboardButton("Til kurslari 📚"), 
				 KeyboardButton("Dasturlash kurslari 👨🏻‍💻")
				]
			   ]

	reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
	update.message.reply_text("Salom siz bu bot orqali quyidagi yo'nalishlarni tanlashingiz mumkin: ",
							   reply_markup=reply_markup)

	users.save_ids(update.message.chat_id)

	global current_position
	current_position = "Home"
	print(current_position)

start_handler = CH('start', start)
dper.add_handler(start_handler)


def til_kurslari(bot, update):
	keyboard = [
				[KeyboardButton("Ingliz tili 🇬🇧")],
				[
				 KeyboardButton("Ortga ⬅️"), 
				 KeyboardButton("Bosh menyu 🏠")
				]
			   ]

	reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
	update.message.reply_text("Mavjud til kurslaridan birini tanlang!",
							  reply_markup=reply_markup)
	global current_position
	current_position = "Langs"
	print(current_position)


def dasturlash_kurslari(bot, update):
	keyboard = [
				[KeyboardButton("Python 🐍")],
				[KeyboardButton("Java 🍵")],
				[
				 KeyboardButton("Ortga ⬅️"), 
				 KeyboardButton("Bosh menyu 🏠")
				]
			   ]

	reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
	update.message.reply_text("Mavjud kurslardan birini tanlang!",
							  reply_markup=reply_markup)

	global current_position
	current_position = "Coding"
	print(current_position)
	

def eng_teachers(bot, update):
	keyboard = [
				[KeyboardButton("Shosalim Bakhtiyorov")],
				[KeyboardButton("Umidjon Sobirov")],
				[
				 KeyboardButton("Ortga ⬅️"), 
				 KeyboardButton("Bosh menyu 🏠")
				]
			   ]

	reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
	update.message.reply_text("Ingliz tilini kim bilan o'rganishni xohlaysiz?",
							  reply_markup=reply_markup)

	global current_position
	current_position = "Teachers"
	print(current_position)


"""

	This is a place for further coding like python courses and so on!

"""








def ortga(bot, update):
	print(current_position)
	if current_position == "Teachers":
		bot.send_message(chat_id=update.message.chat_id, text="Ortga ⬅️")
		til_kurslari(bot, update)
	elif current_position == "Coding" or current_position == "Langs":
		bot.send_message(chat_id=update.message.chat_id, text="Ortga ⬅️")
		start(bot, update)



def tanlovlar(bot, update):
	msg_txt = update.message.text

	if "Til kurslari 📚" in msg_txt:
		til_kurslari(bot, update)
	elif "Dasturlash kurslari 👨🏻‍💻" in msg_txt:
		dasturlash_kurslari(bot, update)
	elif "Ingliz tili 🇬🇧" in msg_txt:
		eng_teachers(bot, update)
	elif "Rus tili "  in msg_txt:
		pass
	elif "Python 🐍" in msg_txt:
		pass
	elif "Ortga ⬅️" in msg_txt:
		ortga(bot, update) 

dper.add_handler(MH(Filters.text, tanlovlar))







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

	if len(msg_txt.split()) > 1:
		if update.message.from_user.id == 137786647:
			for user_id in user_ids:
				try:
					bot.send_message(chat_id=user_id, text=msg_txt[10:])
				except Exception:
					users.remove_ids(user_id)
					pass
		else:
			bot.send_message(chat_id=update.message.chat_id, text="Sorry you don't have access to this command")
	else:
		bot.send_message(chat_id=update.message.chat_id, text="Should contain text to broadcast")


broadcast_handler = CH('broadcast', broadcast)
dper.add_handler(broadcast_handler)


# /help command handler
def help_command(bot, update):
	help_text = "Welcome to Beruny English with Mr.Salim!\n"\
				"I can help you with the assignments given by *Mr.Salim*\n"\
				"/start -> Start the bot!\n"\
				"/help -> This help message!\n"\
				"/tasks -> Get the tasks to practise what you're learning"

	bot.send_message(chat_id=update.message.chat_id, text=help_text, parse_mode=telegram.ParseMode.MARKDOWN)


help_handler = CH('help', help_command)
dper.add_handler(help_handler)

uper.start_polling()