import logging
import users
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
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
# token = "783492460:AAF251KyHEzgS23v_8n1A2mBOyMOBJwyE-4"
uper = Uper(token=token)
dper = uper.dispatcher


global current_position
current_position = "Nothing"

global feedback_id
feedback_id = 12

# /start command responder
def start(bot, update):
	keyboard = [
		[KeyboardButton("Til kurslari 📚"), KeyboardButton("Dasturlash kurslari 👨🏻‍💻")],
		[KeyboardButton("Adminlar bilan bog'lanish")]
	]
	reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
	welcome_txt = "Salom! 👋\nBeruny Academy rasmiy botiga 🤖 xush kelibsiz, sizni bu yerda ko'rganimdan mamnunman! 🤝 \n\n"\
				  "Siz bu bot orqali quyidagi yo'nalishlarni tanlashingiz mumkin:"
	update.message.reply_text(welcome_txt, reply_markup=reply_markup)
	users.save_ids(update.message.chat_id)
	global current_position
	current_position = "Home"


def uy(bot, update):
	keyboard = [
		[KeyboardButton("Til kurslari 📚"), KeyboardButton("Dasturlash kurslari 👨🏻‍💻")],
		[KeyboardButton("Adminlar bilan bog'lanish")]
	]
	reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
	update.message.reply_text("Quyidagi yo'nalishlardan birini tanlang:", reply_markup=reply_markup)
	global current_position
	current_position = "Home"


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
		[KeyboardButton("JavaScript 🔰")],
		[KeyboardButton("Python 🐍")],
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
		 InlineKeyboardButton("6-Dars", callback_data="ue6")],
		[InlineKeyboardButton("7-Dars", callback_data="ue7")]
	]
	reply_markup = InlineKeyboardMarkup(InlineKeyboard)
	update.message.reply_text("Quyidagi darslar ro'yxatidan keraklisini tanlang:", reply_markup=reply_markup)
	global current_position
	current_position = "UmidE"


def salim_ingliz_tili_darajalar(bot, update):  # Should be made changes
	keyboard = [
		[InlineKeyboardButton("Tanishuv 👋", callback_data="tanishuv"),],
	]
	reply_markup = InlineKeyboardMarkup(keyboard, resize_keyboard=True)
	update.message.reply_text("Mavjud ingliz tili darajalaridan birini tanlang:",
							  reply_markup=reply_markup)
	global current_position
	current_position = "Levels"


def javascript(bot, update):
	InlineKeyboard = [
		[InlineKeyboardButton("1-Dars", callback_data="js1"),
		 InlineKeyboardButton("2-Dars", callback_data="js2")],
		[InlineKeyboardButton("3-Dars", callback_data="js3"),
		 InlineKeyboardButton("4-Dars", callback_data="js4")],
		[InlineKeyboardButton("5-Dars", callback_data="js5"),
		 InlineKeyboardButton("6-Dars", callback_data="js6")],
		[InlineKeyboardButton("7-Dars", callback_data="js7"),
		 InlineKeyboardButton("8-Dars", callback_data="js8")],
		[InlineKeyboardButton("9-Dars", callback_data="js9"),
		 InlineKeyboardButton("10-Dars", callback_data="js10")],
		[InlineKeyboardButton("Davomi ⏩", callback_data="jsnext1")]
	]
	reply_markup = InlineKeyboardMarkup(InlineKeyboard)
	update.message.reply_text("Bu darslar Farxod Dadajonov tomonidan tuzilgan va @virtualdars kanalidan olingan!\n"\
							  "Quyidagi darslar ro'yxatidan keraklisini tanlang:", 
		reply_markup=reply_markup)
	global current_position
	current_position = "JavaScript"


def bosh_menyu(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="Bosh menyu 🏠")
	uy(bot, update)


def sending(bot, update):
	bot.edit_message_text(text="Siz so'ragan fayl jonatilyapti! Iltimos biroz kuting!",
						  chat_id=update.callback_query.message.chat_id,
						  message_id=update.callback_query.message.message_id)


def ids(bot, update):
	all_ids = users.file_with_ids()
	bot.send_message(chat_id=update.message.chat_id, text="here is the list of ids: \n{}".format(all_ids))


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


def chat_id(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text=update.message.chat_id)
	pass


def feedback(bot, update):
	keyboard = [
		[KeyboardButton("Bekor qilish"),],
	]

	reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
	bot.send_message(chat_id=update.message.chat_id, 
					 text="Bizga qanday murojatingiz bo'lsa uni yozib qoldirishingiz mumkin.",
					 reply_markup=reply_markup)

	global feedback_id
	feedback_id = update.update_id


def ortga(bot, update):
	if current_position == "Teachers":
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
		uy(bot, update)
	elif current_position == "JavaScript":
		bot.send_message(chat_id=update.message.chat_id, text="Ortga ⬅️")
		uy(bot, update)


def tanlovlar(bot, update):
	msg_txt = update.message.text
	global feedback_id

	if (update.update_id - 1) == feedback_id and msg_txt != "Bekor qilish":
		bot.forward_message(chat_id=137786647,
		    				from_chat_id=update.message.chat_id,
			    			message_id=update.message.message_id)
		bot.send_message(chat_id=update.message.chat_id,
						 text="Sizning xabaringiz adminlarga jo'natildi! Tez orada ular siz bilan bog'lanishadi!")
		uy(bot, update)

	if "Adminlar bilan bog'lanish" == msg_txt:
		feedback(bot, update)
	elif "Til kurslari 📚" == msg_txt:
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
	elif "Dasturlash kurslari 👨🏻‍💻" == msg_txt:
		dasturlash_kurslari(bot, update)
	elif "JavaScript 🔰" == msg_txt:
		javascript(bot, update)
	elif "Python 🐍" == msg_txt:
		pass
	elif "Ortga ⬅️" == msg_txt:
		ortga(bot, update)
	elif "Bosh menyu 🏠" == msg_txt:
		bosh_menyu(bot, update)
	elif "Bekor qilish" == msg_txt:
		bot.send_message(text="Bekor qilindi",
						 chat_id=update.message.chat_id,
						 message_id=update.message.message_id)
		uy(bot, update)


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
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/14",
					   caption="Beginner {}-Dars.\n Umidjon Sobirov".format(query.data[2:]))
	elif query.data == "ub2":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/22",
					   caption="Beginner {}-Dars.\n Umidjon Sobirov".format(query.data[2:]))
	elif query.data == "ub3":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/28",
					   caption="Beginner {}-Dars.\n Umidjon Sobirov".format(query.data[2:]))
	elif query.data == "ub4":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/42",
					   caption="Beginner {}-Dars.\n Umidjon Sobirov".format(query.data[2:]))
	elif query.data == "ub5":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/47",
					   caption="Beginner {}-Dars.\n Umidjon Sobirov".format(query.data[2:]))
	elif query.data == "ub6":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/55",
					   caption="Beginner {}-Dars.\n Umidjon Sobirov".format(query.data[2:]))
	elif query.data == "ub7":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/57",
					   caption="Beginner {}-Dars.\n Umidjon Sobirov".format(query.data[2:]))
	elif query.data == "ub8":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/70",
					   caption="Beginner {}-Dars.\n Umidjon Sobirov".format(query.data[2:]))
	elif query.data == "ub9":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/85",
					   caption="Beginner {}-Dars.\n Umidjon Sobirov".format(query.data[2:]))
	elif query.data == "ub10":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/90",
					   caption="Beginner {}-Dars.\n Umidjon Sobirov".format(query.data[2:]))
	elif query.data == "ub11":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/141",
					   caption="Beginner {}-Dars.\n Umidjon Sobirov".format(query.data[2:]))
	elif query.data == "ub12":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/147",
					   caption="Beginner {}-Dars.\n Umidjon Sobirov".format(query.data[2:]))
	elif query.data == "ub13":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/153",
					   caption="Beginner {}-Dars.\n Umidjon Sobirov".format(query.data[2:]))
	elif query.data == "ub14":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/162",
					   caption="Beginner {}-Dars.\n Umidjon Sobirov".format(query.data[2:]))
	elif query.data == "ub15":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/172",
					   caption="Beginner {}-Dars.\n Umidjon Sobirov".format(query.data[2:]))
	elif query.data == "ub16":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/177",
					   caption="Beginner {}-Dars.\n Umidjon Sobirov".format(query.data[2:]))
	elif query.data == "ub17":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/183",
					   caption="Beginner {}-Dars.\n Umidjon Sobirov".format(query.data[2:]))
	elif query.data == "ub18":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/192",
					   caption="Beginner {}-Dars.\n Umidjon Sobirov".format(query.data[2:]))
	elif query.data == "ub19":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/203",
					   caption="Beginner {}-Dars.\n Umidjon Sobirov".format(query.data[2:]))
	elif query.data == "ub20":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/216",
					   caption="Beginner {}-Dars.\n Umidjon Sobirov".format(query.data[2:]))
	elif query.data == "ub21":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/233",
					   caption="Beginner {}-Dars.\n Umidjon Sobirov".format(query.data[2:]))
	elif query.data == "ub22":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/237",
					   caption="Beginner {}-Dars.\n Umidjon Sobirov".format(query.data[2:]))
	elif query.data == "ub23":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/239",
					   caption="Beginner {}-Dars.\n Umidjon Sobirov".format(query.data[2:]))
	elif query.data == "ub24":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/248",
					   caption="Beginner {}-Dars.\n Umidjon Sobirov".format(query.data[2:]))
	elif query.data == "ub25":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/249",
					   caption="Beginner {}-Dars.\n Umidjon Sobirov".format(query.data[2:]))
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
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/343",
					   caption="Elementary {}-Dars.\nUmidjon Sobirov".format(query.data[2:]))
	elif query.data == "ue2":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/354",
					   caption="Elementary {}-Dars.\nUmidjon Sobirov".format(query.data[2:]))
	elif query.data == "ue3":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/361",
					   caption="Elementary {}-Dars.\nUmidjon Sobirov".format(query.data[2:]))
	elif query.data == "ue4":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/370",
					   caption="Elementary {}-Dars.\nUmidjon Sobirov".format(query.data[2:]))
	elif query.data == "ue5":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/376",
					   caption="Elementary {}-Dars.\nUmidjon Sobirov".format(query.data[2:]))
	elif query.data == "ue6":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/385",
					   caption="Elementary {}-Dars.\nUmidjon Sobirov".format(query.data[2:]))
	elif query.data == "ue7":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/410",
					   caption="Elementary {}-Dars.\nUmidjon Sobirov".format(query.data[2:])) # Things should be continued from here to the rest
	elif query.data == "ue8":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/70",
					   caption="Elementary {}-Dars.\nUmidjon Sobirov".format(query.data[2:]))
	elif query.data == "ue9":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/85",
					   caption="Elementary {}-Dars.\nUmidjon Sobirov".format(query.data[2:]))
	elif query.data == "ue10":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/90",
					   caption="Elementary {}-Dars.\nUmidjon Sobirov".format(query.data[2:]))
	elif query.data == "ue11":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/141",
					   caption="Elementary {}-Dars.\nUmidjon Sobirov".format(query.data[2:]))
	elif query.data == "ue12":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/147",
					   caption="Elementary {}-Dars.\nUmidjon Sobirov".format(query.data[2:]))
	elif query.data == "ue13":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/153",
					   caption="Elementary {}-Dars.\nUmidjon Sobirov".format(query.data[2:]))
	elif query.data == "ue14":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/162",
					   caption="Elementary {}-Dars.\nUmidjon Sobirov".format(query.data[2:]))
	elif query.data == "ue15":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/172",
					   caption="Elementary {}-Dars.\nUmidjon Sobirov".format(query.data[2:]))
	elif query.data == "ue16":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/177",
					   caption="Elementary {}-Dars.\nUmidjon Sobirov".format(query.data[2:]))
	elif query.data == "ue17":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/183",
					   caption="Elementary {}-Dars.\nUmidjon Sobirov".format(query.data[2:]))
	elif query.data == "ue18":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/192",
					   caption="Elementary {}-Dars.\nUmidjon Sobirov".format(query.data[2:]))
	elif query.data == "ue19":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/203",
					   caption="Elementary {}-Dars.\nUmidjon Sobirov".format(query.data[2:]))
	elif query.data == "ue20":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/216",
					   caption="Elementary {}-Dars.\nUmidjon Sobirov".format(query.data[2:]))
	elif query.data == "ue21":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/233",
					   caption="Elementary {}-Dars.\nUmidjon Sobirov".format(query.data[2:]))
	elif query.data == "ue22":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/237",
					   caption="Elementary {}-Dars.\nUmidjon Sobirov".format(query.data[2:]))
	elif query.data == "ue23":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/239",
					   caption="Elementary {}-Dars.\nUmidjon Sobirov".format(query.data[2:]))
	elif query.data == "ue24":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/248",
					   caption="Elementary {}-Dars.\nUmidjon Sobirov".format(query.data[2:]))
	elif query.data == "ue25":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/BerunyBeginner/249",
					   caption="Elementary {}-Dars.\nUmidjon Sobirov".format(query.data[2:]))
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

	# Query responder for my introduction video

	if query.data == "tanishuv":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id, "https://t.me/testberuny/2")


	# Query responder for JS lessons starts

	InlineKeyboardJS = [
		[InlineKeyboardButton("1-Dars", callback_data="js1"),
		 InlineKeyboardButton("2-Dars", callback_data="js2")],
		[InlineKeyboardButton("3-Dars", callback_data="js3"),
		 InlineKeyboardButton("4-Dars", callback_data="js4")],
		[InlineKeyboardButton("5-Dars", callback_data="js5"),
		 InlineKeyboardButton("6-Dars", callback_data="js6")],
		[InlineKeyboardButton("7-Dars", callback_data="js7"),
		 InlineKeyboardButton("8-Dars", callback_data="js8")],
		[InlineKeyboardButton("9-Dars", callback_data="js9"),
		 InlineKeyboardButton("10-Dars", callback_data="js10")],
		[InlineKeyboardButton("Davomi ⏩", callback_data="jsnext1")]
	]
	reply_markup_js = InlineKeyboardMarkup(InlineKeyboardJS)

	InlineKeyboardJS1 = [
		[InlineKeyboardButton("11-Dars 1-Qism", callback_data="js11a")],
		[InlineKeyboardButton("11-Dars (2)", callback_data="js11b"),
		 InlineKeyboardButton("12-Dars", callback_data="js12")],
		[InlineKeyboardButton("13-Dars", callback_data="js13"),
		 InlineKeyboardButton("14-Dars", callback_data="js14")],
		[InlineKeyboardButton("15-Dars", callback_data="js15"),
		 InlineKeyboardButton("16-Dars", callback_data="js16")],
		[InlineKeyboardButton("17-Dars", callback_data="js17"),
		 InlineKeyboardButton("18-Dars", callback_data="js18")],
		[InlineKeyboardButton("19-Dars", callback_data="js19"),
		 InlineKeyboardButton("20-Dars", callback_data="js20")],
		[InlineKeyboardButton("Avvalgisi ⏪", callback_data="jsprev1"),
		 InlineKeyboardButton("Davomi ⏩", callback_data="jsnext2")]
	]
	reply_markup_js1 = InlineKeyboardMarkup(InlineKeyboardJS1)

	InlineKeyboardJS2 = [
		[InlineKeyboardButton("21-Dars", callback_data="js21"),
		 InlineKeyboardButton("22-Dars", callback_data="js22")],
		[InlineKeyboardButton("23-Dars", callback_data="js23"),
		 InlineKeyboardButton("24-Dars", callback_data="js24")],
		[InlineKeyboardButton("25-Dars 1-Qism", callback_data="js25a"),],
		[InlineKeyboardButton("25-Dars (2)", callback_data="js25b"),
		 InlineKeyboardButton("26-Dars", callback_data="js26")],
		[InlineKeyboardButton("27-Dars", callback_data="js27"),
		 InlineKeyboardButton("28-Dars", callback_data="js28")],
		[InlineKeyboardButton("29-Dars", callback_data="js29"),
		 InlineKeyboardButton("30-Dars", callback_data="js30")],
		[InlineKeyboardButton("Avvalgisi ⏪", callback_data="jsprev2"),
		 InlineKeyboardButton("Davomi ⏩", callback_data="jsnext3")]
	]
	reply_markup_js2 = InlineKeyboardMarkup(InlineKeyboardJS2)

	InlineKeyboardJS3 = [
		[InlineKeyboardButton("31-Dars", callback_data="js31"),
		 InlineKeyboardButton("32-Dars", callback_data="js32")],
		[InlineKeyboardButton("33-Dars", callback_data="js33"),
		 InlineKeyboardButton("34-Dars", callback_data="js34")],
		[InlineKeyboardButton("35-Dars", callback_data="js35"),
		 InlineKeyboardButton("36-Dars", callback_data="js36")],
		[InlineKeyboardButton("37-Dars", callback_data="js37"),
		 InlineKeyboardButton("38-Dars", callback_data="js38")],
		[InlineKeyboardButton("39-Dars", callback_data="js39"),
		 InlineKeyboardButton("40-Dars", callback_data="js40")],
		[InlineKeyboardButton("Avvalgisi ⏪", callback_data="jsprev3"),
		 InlineKeyboardButton("Davomi ⏩", callback_data="jsnext4")]
	]
	reply_markup_js3 = InlineKeyboardMarkup(InlineKeyboardJS3)

	InlineKeyboardJS4 = [
		[InlineKeyboardButton("41-Dars", callback_data="js41"),
		 InlineKeyboardButton("42-Dars", callback_data="js42")],
		[InlineKeyboardButton("43-Dars", callback_data="js43"),
		 InlineKeyboardButton("44-Dars", callback_data="js44")],
		[InlineKeyboardButton("45-Dars", callback_data="js45"),
		 InlineKeyboardButton("46-Dars", callback_data="js46")],
		[InlineKeyboardButton("47-Dars", callback_data="js47"),
		 InlineKeyboardButton("48-Dars", callback_data="js48")],
		[InlineKeyboardButton("49-Dars", callback_data="js49"),
		 InlineKeyboardButton("50-Dars", callback_data="js50")],
		[InlineKeyboardButton("51-Dars", callback_data="js51"),
		 InlineKeyboardButton("52-Dars", callback_data="js52")],
		[InlineKeyboardButton("Avvalgisi ⏪", callback_data="jsprev4"),]
	]
	reply_markup_js4 = InlineKeyboardMarkup(InlineKeyboardJS4)



	if query.data == "js1":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/165", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js2":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/168", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js3":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/169", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js4":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/170", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js5":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/171", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js6":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/172", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js7":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/173", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js8":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/174", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js9":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/175", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js10":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/176", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js11a":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/177", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js11b":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/178", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js12":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/179", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js13":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/181", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js14":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/182", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js15":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/183", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js16":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/184", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js17":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/185", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js18":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/186", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js19":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/187", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js20":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/188", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js21":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/189", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js22":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/190", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js23":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/191", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js24":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/192", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js25a":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/193", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js25b":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/194", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js26":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/195", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js27":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/196", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js28":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/198", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js29":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/199", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js30":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/200", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js31":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/201", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js32":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/202", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js33":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/203", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js34":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/204", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js35":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/205", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js36":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/206", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js37":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/207", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js38":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/208", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js39":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/209", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js40":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/211", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js41":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/212", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js42":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/213", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js43":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/214", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js44":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/215", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js45":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/216", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js46":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/217", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js47":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/219", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js48":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/221", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js49":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/222", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js50":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/223", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js51":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/224", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "js52":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/virtualdars/225", 
					   caption="JavaScript {}-Dars".format(query.data[2:]))
	elif query.data == "jsnext1":
		bot.edit_message_text(text="Quyidagi darslar ro'yxatidan keraklisini tanlang:",
							  chat_id=update.callback_query.message.chat_id,
							  message_id=update.callback_query.message.message_id,
							  reply_markup=reply_markup_js1
							)
	elif query.data == "jsnext2":
		bot.edit_message_text(text="Quyidagi darslar ro'yxatidan keraklisini tanlang:",
							  chat_id=update.callback_query.message.chat_id,
							  message_id=update.callback_query.message.message_id,
							  reply_markup=reply_markup_js2
							)
	elif query.data == "jsnext3":
		bot.edit_message_text(text="Quyidagi darslar ro'yxatidan keraklisini tanlang:",
							  chat_id=update.callback_query.message.chat_id,
							  message_id=update.callback_query.message.message_id,
							  reply_markup=reply_markup_js3
							)
	elif query.data == "jsnext4":
		bot.edit_message_text(text="Quyidagi darslar ro'yxatidan keraklisini tanlang:",
							  chat_id=update.callback_query.message.chat_id,
							  message_id=update.callback_query.message.message_id,
							  reply_markup=reply_markup_js4
							)
	elif query.data == "jsprev1":
		bot.edit_message_text(text="Quyidagi darslar ro'yxatidan keraklisini tanlang:",
							  chat_id=update.callback_query.message.chat_id,
							  message_id=update.callback_query.message.message_id,
							  reply_markup=reply_markup_js
							)
	elif query.data == "jsprev2":
		bot.edit_message_text(text="Quyidagi darslar ro'yxatidan keraklisini tanlang:",
							  chat_id=update.callback_query.message.chat_id,
							  message_id=update.callback_query.message.message_id,
							  reply_markup=reply_markup_js1
							)
	elif query.data == "jsprev3":
		bot.edit_message_text(text="Quyidagi darslar ro'yxatidan keraklisini tanlang:",
							  chat_id=update.callback_query.message.chat_id,
							  message_id=update.callback_query.message.message_id,
							  reply_markup=reply_markup_js2
							)
	elif query.data == "jsprev4":
		bot.edit_message_text(text="Quyidagi darslar ro'yxatidan keraklisini tanlang:",
							  chat_id=update.callback_query.message.chat_id,
							  message_id=update.callback_query.message.message_id,
							  reply_markup=reply_markup_js3
							)
	if query.data == "bekor_qilish":
		bot.edit_message_text(text="Bekor qilindi",
							  chat_id=update.callback_query.message.chat_id,
							  message_id=update.callback_query.message.message_id
							)


start_handler = CH('start', start)
broadcast_handler = CH('broadcast', broadcast)
ids_handler = CH('ids', ids)
dper.add_handler(ids_handler)
dper.add_handler(start_handler)
dper.add_handler(CH('id', chat_id))
dper.add_handler(broadcast_handler)
dper.add_handler(MH(Filters.text, tanlovlar))

import os
PORT = os.environ.get('PORT')
uper.start_webhook(listen="0.0.0",
				   port=int(PORT),
				   url_path=token)
uper.bot.setWebhook("https://beruny-bot.herokuapp.com/{}".format(token))
uper.idle()