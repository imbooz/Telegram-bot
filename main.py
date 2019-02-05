import logging
import users
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
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

# /start command responder
def start(bot, update):
	keyboard = [
		[KeyboardButton("Til kurslari 📚"), KeyboardButton("Dasturlash kurslari 👨🏻‍💻")],
	]
	reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
	welcome_txt = "Salom! 👋\nBeruny Academy rasmiy botiga 🤖 xush kelibsiz, sizni bu yerda ko'rganimdan mamnunman! 🤝 \n\n"\
				  "Siz bu bot orqali quyidagi yo'nalishlarni tanlashingiz mumkin:"
	update.message.reply_text(welcome_txt, reply_markup=reply_markup)
	users.save_ids(update.message.chat_id)
	global current_position
	current_position = "Home"


start_handler = CH('start', start)
dper.add_handler(start_handler)


def til_kurslari(bot, update):
	keyboard = [
		[KeyboardButton("Ingliz tili 🇬🇧")],
		[KeyboardButton("Ortga ⬅️"), KeyboardButton("Bosh menyu 🏠")]
	]
	reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
	update.message.reply_text("Mavjud til kurslaridan birini tanlang!",
							  reply_markup=reply_markup)
	global current_position
	current_position = "Langs"


def dasturlash_kurslari(bot, update):
	keyboard = [
		[KeyboardButton("Python 🐍")],
		[KeyboardButton("JavaScript 🔰")],
		[KeyboardButton("Ortga ⬅️"), KeyboardButton("Bosh menyu 🏠")]
    ]
	reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
	update.message.reply_text("Mavjud kurslardan birini tanlang!",
							  reply_markup=reply_markup)
	global current_position
	current_position = "Coding"
	

def ustozlar_ingliz_tili(bot, update):
	keyboard = [
		[KeyboardButton("Shosalim Bakhtiyorov 👨🏻‍🏫")],
		[KeyboardButton("Umidjon Sobirov 👨🏻‍🏫")],
		[KeyboardButton("Ortga ⬅️"), KeyboardButton("Bosh menyu 🏠")]
	]
	reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
	update.message.reply_text("Ingliz tilini kim bilan o'rganishni xohlaysiz?",
							  reply_markup=reply_markup)
	global current_position
	current_position = "Teachers"


def umid_ingliz_tili_darajalar(bot, update):
	keyboard = [
		[KeyboardButton("Beginner"),],
		[KeyboardButton("Elementary"),],
		[KeyboardButton("Ortga ⬅️"), KeyboardButton("Bosh menyu 🏠")]
	]
	reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
	update.message.reply_text("Mavjud ingliz darajalaridan birini tanlang:",
							  reply_markup=reply_markup)
	global current_position
	current_position = "Levels"


def umid_beginner(bot, update):
	InlineKeyboard = [
		[InlineKeyboardButton("1-Dars", callback_data="ub1"),
		 InlineKeyboardButton("2-Dars", callback_data="ub2")],
		[InlineKeyboardButton("3-Dars", callback_data="ub3"),
		 InlineKeyboardButton("4-Dars", callback_data="ub4")],
		[InlineKeyboardButton("5-Dars", callback_data="ub5"),
		 InlineKeyboardButton("6-Dars", callback_data="ub6")],
		[InlineKeyboardButton("7-Dars", callback_data="ub7"),
		 InlineKeyboardButton("8-Dars", callback_data="ub8")],
		[InlineKeyboardButton("9-Dars", callback_data="ub9"),
		 InlineKeyboardButton("10-Dars", callback_data="ub10")],
		[InlineKeyboardButton("Davomi ⏩", callback_data="ubnext1")]
	]
	reply_markup = InlineKeyboardMarkup(InlineKeyboard)
	update.message.reply_text("Quyidagi darslar ro'yxatidan keraklisini tanlang:", reply_markup=reply_markup)
	global current_position
	current_position = "UmidB"


def umid_elementary(bot, update):
	InlineKeyboard = [
		[InlineKeyboardButton("1-Dars", callback_data="ue1"),
		 InlineKeyboardButton("2-Dars", callback_data="ue2")],
		[InlineKeyboardButton("3-Dars", callback_data="ue3"),
		 InlineKeyboardButton("4-Dars", callback_data="ue4")],
		[InlineKeyboardButton("5-Dars", callback_data="ue5"),
		 InlineKeyboardButton("6-Dars", callback_data="ue6")]
	]
	reply_markup = InlineKeyboardMarkup(InlineKeyboard)
	update.message.reply_text("Quyidagi darslar ro'yxatidan keraklisini tanlang:", reply_markup=reply_markup)
	global current_position
	current_position = "UmidE"


def salim_ingliz_tili_darajalar(bot, update):
	keyboard = [
		[KeyboardButton("Beginner 👶"),],
	]
	reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
	update.message.reply_text("Mavjud ingliz tili darajalaridan birini tanlang:",
							  reply_markup=reply_markup)
	global current_position
	current_position = "Levels"

"""

	This is a place for further coding like python courses and so on!

"""






def bosh_menyu(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="Bosh menyu 🏠")
	start(bot, update)


def ortga(bot, update):
	elif current_position == "Teachers":
		bot.send_message(chat_id=update.message.chat_id, text="Ortga ⬅️")
		til_kurslari(bot, update)
	elif current_position == "Levels":
		bot.send_message(chat_id=update.message.chat_id, text="Ortga ⬅️")
		ustozlar_ingliz_tili(bot, update)
	elif current_position == "UmidB" or current_position == "UmidE":
		bot.send_message(chat_id=update.message.chat_id, text="Ortga ⬅️")
		umid_ingliz_tili_darajalar(bot, update)
	elif current_position == "Coding" or current_position == "Langs":
		bot.send_message(chat_id=update.message.chat_id, text="Ortga ⬅️")
		start(bot, update)


def tanlovlar(bot, update):
	msg_txt = update.message.text

	if "Til kurslari 📚" == msg_txt:
		til_kurslari(bot, update)
	elif "Ingliz tili 🇬🇧" == msg_txt:
		ustozlar_ingliz_tili(bot, update)
	elif "Umidjon Sobirov 👨🏻‍🏫" == msg_txt:
		umid_ingliz_tili_darajalar(bot, update)
	elif "Beginner" == msg_txt:
		umid_beginner(bot, update)
	elif "Elementary" == msg_txt:
		umid_elementary(bot, update)
	elif "Shosalim Bakhtiyorov 👨🏻‍🏫" == msg_txt:
		salim_ingliz_tili_darajalar(bot, update)
	elif "Rus tili "  == msg_txt:
		pass
	elif "Python 🐍" == msg_txt:
		pass
	elif "Dasturlash kurslari 👨🏻‍💻" == msg_txt:
		dasturlash_kurslari(bot, update)
	elif "Ortga ⬅️" == msg_txt:
		ortga(bot, update)
	elif "Bosh menyu 🏠" == msg_txt:
		bosh_menyu(bot, update) 

dper.add_handler(MH(Filters.text, tanlovlar))



def sending(bot, update):
	bot.edit_message_text(text="Siz so'ragan fayl jonatilyapti! Iltimos biroz kuting!",
							  chat_id=update.callback_query.message.chat_id,
							  message_id=update.callback_query.message.message_id
							)


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



def darsalar_uchun_query(bot, update):

	# Query responder for Umid's beginner lessons starts

	query = update.callback_query
	InlineKeyboardBeg = [
		[InlineKeyboardButton("1-Dars", callback_data="ub1"),
		 InlineKeyboardButton("2-Dars", callback_data="ub2")],
		[InlineKeyboardButton("3-Dars", callback_data="ub3"),
		 InlineKeyboardButton("4-Dars", callback_data="ub4")],
		[InlineKeyboardButton("5-Dars", callback_data="ub5"),
		 InlineKeyboardButton("6-Dars", callback_data="ub6")],
		[InlineKeyboardButton("7-Dars", callback_data="ub7"),
		 InlineKeyboardButton("8-Dars", callback_data="ub8")],
		[InlineKeyboardButton("9-Dars", callback_data="ub9"),
		 InlineKeyboardButton("10-Dars", callback_data="ub10")],
		[InlineKeyboardButton("Davomi ⏩", callback_data="ubnext1")]
	]
	reply_markup_beg = InlineKeyboardMarkup(InlineKeyboardBeg)

	InlineKeyboardBeg1 = [
		[InlineKeyboardButton("11-Dars", callback_data="ub11"),
		 InlineKeyboardButton("12-Dars", callback_data="ub12")],
		[InlineKeyboardButton("13-Dars", callback_data="ub13"),
		 InlineKeyboardButton("14-Dars", callback_data="ub14")],
		[InlineKeyboardButton("15-Dars", callback_data="ub15"),
		 InlineKeyboardButton("16-Dars", callback_data="ub16")],
		[InlineKeyboardButton("17-Dars", callback_data="ub17"),
		 InlineKeyboardButton("18-Dars", callback_data="ub18")],
		[InlineKeyboardButton("19-Dars", callback_data="ub19"),
		 InlineKeyboardButton("20-Dars", callback_data="ub20")],
		[InlineKeyboardButton("Avvalgisi ⏪", callback_data="ubprev1"),
		 InlineKeyboardButton("Davomi ⏩", callback_data="ubnext2")]
	]
	reply_markup_beg1 = InlineKeyboardMarkup(InlineKeyboardBeg1)

	InlineKeyboardBeg2 = [
		[InlineKeyboardButton("21-Dars", callback_data="ub21"),],
		[InlineKeyboardButton("22-Dars", callback_data="ub22"),],
		[InlineKeyboardButton("23-Dars", callback_data="ub23"),],
		[InlineKeyboardButton("24-Dars", callback_data="ub24"),],
		[InlineKeyboardButton("25-Dars", callback_data="ub25"),],
		[InlineKeyboardButton("Avvalgisi ⏪", callback_data="ubprev2")]
	]
	reply_markup_beg2 = InlineKeyboardMarkup(InlineKeyboardBeg2)

	if query.data == "ub1":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/14")
	elif query.data == "ub2":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/22")
	elif query.data == "ub3":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/28")
	elif query.data == "ub4":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/42")
	elif query.data == "ub5":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/47")
	elif query.data == "ub6":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/55")
	elif query.data == "ub7":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/57")
	elif query.data == "ub8":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/70")
	elif query.data == "ub9":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/85")
	elif query.data == "ub10":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/90")
	elif query.data == "ub11":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/141")
	elif query.data == "ub12":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/147")
	elif query.data == "ub13":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/153")
	elif query.data == "ub14":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/162")
	elif query.data == "ub15":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/172")
	elif query.data == "ub16":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/177")
	elif query.data == "ub17":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/183")
	elif query.data == "ub18":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/192")
	elif query.data == "ub19":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/203")
	elif query.data == "ub20":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/216")
	elif query.data == "ub21":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/233")
	elif query.data == "ub22":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/237")
	elif query.data == "ub23":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/239")
	elif query.data == "ub24":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/248")
	elif query.data == "ub25":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/249")
	elif query.data == "ubnext1":
		bot.edit_message_text(text="Quyidagi darslar ro'yxatidan keraklisini tanlang:",
							  chat_id=update.callback_query.message.chat_id,
							  message_id=update.callback_query.message.message_id,
							  reply_markup=reply_markup_beg1
							)
	elif query.data == "ubnext2":
		bot.edit_message_text(text="Quyidagi darslar ro'yxatidan keraklisini tanlang:",
							  chat_id=update.callback_query.message.chat_id,
							  message_id=update.callback_query.message.message_id,
							  reply_markup=reply_markup_beg2
							)
	elif query.data == "ubprev1":
		bot.edit_message_text(text="Quyidagi darslar ro'yxatidan keraklisini tanlang:",
							  chat_id=update.callback_query.message.chat_id,
							  message_id=update.callback_query.message.message_id,
							  reply_markup=reply_markup_beg
							)
	elif query.data == "ubprev2":
		bot.edit_message_text(text="Quyidagi darslar ro'yxatidan keraklisini tanlang:",
							  chat_id=update.callback_query.message.chat_id,
							  message_id=update.callback_query.message.message_id,
							  reply_markup=reply_markup_beg1
							)

	# Query responder for Umid's beginner lessons ends

	"""/////////////////////////////////////////////////////////////////////////////////////"""

	# Query responder for Umid's elementary lessons starts

	InlineKeyboardElem = [
		[InlineKeyboardButton("1-Dars", callback_data="ue1"),
		 InlineKeyboardButton("2-Dars", callback_data="ue2")],
		[InlineKeyboardButton("3-Dars", callback_data="ue3"),
		 InlineKeyboardButton("4-Dars", callback_data="ue4")],
		[InlineKeyboardButton("5-Dars", callback_data="ue5"),
		 InlineKeyboardButton("6-Dars", callback_data="ue6")],
		[InlineKeyboardButton("7-Dars", callback_data="ue7"),
		 InlineKeyboardButton("8-Dars", callback_data="ue8")],
		[InlineKeyboardButton("9-Dars", callback_data="ue9"),
		 InlineKeyboardButton("10-Dars", callback_data="ue10")],
		[InlineKeyboardButton("Davomi ⏩", callback_data="uenext1")]
	]
	reply_markup_elem = InlineKeyboardMarkup(InlineKeyboardElem)

	InlineKeyboardElem1 = [
		[InlineKeyboardButton("11-Dars", callback_data="ue11"),
		 InlineKeyboardButton("12-Dars", callback_data="ue12")],
		[InlineKeyboardButton("13-Dars", callback_data="ue13"),
		 InlineKeyboardButton("14-Dars", callback_data="ue14")],
		[InlineKeyboardButton("15-Dars", callback_data="ue15"),
		 InlineKeyboardButton("16-Dars", callback_data="ue16")],
		[InlineKeyboardButton("17-Dars", callback_data="ue17"),
		 InlineKeyboardButton("18-Dars", callback_data="ue18")],
		[InlineKeyboardButton("19-Dars", callback_data="ue19"),
		 InlineKeyboardButton("20-Dars", callback_data="ue20")],
		[InlineKeyboardButton("Avvalgisi ⏪", callback_data="ueprev1"),
		 InlineKeyboardButton("Davomi ⏩", callback_data="uenext2")]
	]
	reply_markup_elem1 = InlineKeyboardMarkup(InlineKeyboardElem1)

	InlineKeyboardElem2 = [
		[InlineKeyboardButton("21-Dars", callback_data="ue21"),],
		[InlineKeyboardButton("22-Dars", callback_data="ue22"),],
		[InlineKeyboardButton("23-Dars", callback_data="ue23"),],
		[InlineKeyboardButton("24-Dars", callback_data="ue24"),],
		[InlineKeyboardButton("25-Dars", callback_data="ue25"),],
		[InlineKeyboardButton("Avvalgisi ⏪", callback_data="ueprev2")]
	]
	reply_markup_elem = InlineKeyboardMarkup(InlineKeyboardElem2)

	if query.data == "ue1":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/343")
	elif query.data == "ue2":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/354")
	elif query.data == "ue3":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/361")
	elif query.data == "ue4":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/370")
	elif query.data == "ue5":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/376")
	elif query.data == "ue6":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/385")
	elif query.data == "ue7":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/57") # Things should be continued from here to the rest
	elif query.data == "ue8":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/70")
	elif query.data == "ue9":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/85")
	elif query.data == "ue10":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/90")
	elif query.data == "ue11":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/141")
	elif query.data == "ue12":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/147")
	elif query.data == "ue13":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/153")
	elif query.data == "ue14":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/162")
	elif query.data == "ue15":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/172")
	elif query.data == "ue16":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/177")
	elif query.data == "ue17":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/183")
	elif query.data == "ue18":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/192")
	elif query.data == "ue19":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/203")
	elif query.data == "ue20":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/216")
	elif query.data == "ue21":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/233")
	elif query.data == "ue22":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/237")
	elif query.data == "ue23":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/239")
	elif query.data == "ue24":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/248")
	elif query.data == "ue25":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/BerunyBeginner/249")
	elif query.data == "uenext1":
		bot.edit_message_text(text="Quyidagi darslar ro'yxatidan keraklisini tanlang:",
							  chat_id=update.callback_query.message.chat_id,
							  message_id=update.callback_query.message.message_id,
							  reply_markup=reply_markup_elem1
							)
	elif query.data == "uenext2":
		bot.edit_message_text(text="Quyidagi darslar ro'yxatidan keraklisini tanlang:",
							  chat_id=update.callback_query.message.chat_id,
							  message_id=update.callback_query.message.message_id,
							  reply_markup=reply_markup_elem
							)
	elif query.data == "ueprev1":
		bot.edit_message_text(text="Quyidagi darslar ro'yxatidan keraklisini tanlang:",
							  chat_id=update.callback_query.message.chat_id,
							  message_id=update.callback_query.message.message_id,
							  reply_markup=reply_markup_elem
							)
	elif query.data == "ueprev2":
		bot.edit_message_text(text="Quyidagi darslar ro'yxatidan keraklisini tanlang:",
							  chat_id=update.callback_query.message.chat_id,
							  message_id=update.callback_query.message.message_id,
							  reply_markup=reply_markup_elem1
							)

	# Query responder for Umid's elementary lessons ends


dper.add_handler(CQH(darsalar_uchun_query))



uper.start_polling()