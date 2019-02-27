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
	welcome_txt = "Salom! 👋\n\nBeruny Academy rasmiy botiga xush kelibsiz, sizni bu yerda ko'rganimdan mamnunman! 🤝 \n\n"\
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
		[KeyboardButton("JavaScript 🔰"), KeyboardButton("Python 🐍")],
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
		[InlineKeyboardButton("5-Dars", callback_data="ub5"),],
		[InlineKeyboardButton("YouTube", url="https://www.youtube.com/playlist?list=PLdNKI0sOr3EX4QygHtKwNVxAVPDpkeFGC"),
		 InlineKeyboardButton("Mover(TAS-IX)", url="https://mover.uz/watch/sIHAnn8m/?list=5YwXxcgo")],
		[InlineKeyboardButton("Beruny.uz", url="http://beruny.uz/index.php/kurslar/course/eng-beginner")]
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
		[InlineKeyboardButton("5-Dars", callback_data="ue5"),],
		[InlineKeyboardButton("YouTube", url="https://www.youtube.com/playlist?list=PLdNKI0sOr3EUhOpqI50EaoWe7vwVey586"),
		 InlineKeyboardButton("Mover(TAS-IX)", url="https://mover.uz/watch/1Q5Los8m/?list=nqRRF3he")],
		[InlineKeyboardButton("Beruny.uz", url="http://beruny.uz/index.php/kurslar/course/english-elementary")]
	]
	reply_markup = InlineKeyboardMarkup(InlineKeyboard)
	update.message.reply_text("Quyidagi darslar ro'yxatidan keraklisini tanlang:", reply_markup=reply_markup)
	global current_position
	current_position = "UmidE"


def salim_ingliz_tili_darajalari(bot, update):
	keyboard = [
		[KeyboardButton("Beginner 👶"),],
		[KeyboardButton("Ortga ⬅️"), KeyboardButton("Bosh menyu 🏠")]
	]
	reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
	update.message.reply_text("Mavjud ingliz tili darajalaridan birini tanlang:",
							  reply_markup=reply_markup)
	global current_position
	current_position = "Levels"


def salim_beginner(bot, update):
	InlineKeyboard = [
		[InlineKeyboardButton("Kurs bilan tanishuv", callback_data="tanishuv"),],
		[InlineKeyboardButton("1-Dars", callback_data="sb1"),
		 InlineKeyboardButton("2-Dars", callback_data="sb2")],
		[InlineKeyboardButton("3-Dars", callback_data="sb3"),
		 InlineKeyboardButton("4-Dars", callback_data="sb4")],
		[InlineKeyboardButton("5-Dars", callback_data="sb5"),],
		[InlineKeyboardButton("YouTube", url="https://www.youtube.com/playlist?list=PLdNKI0sOr3EX4QygHtKwNVxAVPDpkeFGC"), # Should be changed
		 InlineKeyboardButton("Mover(TAS-IX)", url="https://mover.uz/watch/sIHAnn8m/?list=5YwXxcgo")], # Should be changed
		[InlineKeyboardButton("Beruny.uz", url="http://beruny.uz/index.php/kurslar/course/eng-beginner")] # Should be changed
	]
	reply_markup = InlineKeyboardMarkup(InlineKeyboard)
	update.message.reply_text("Quyidagi darslar ro'yxatidan keraklisini tanlang:", reply_markup=reply_markup)
	global current_position
	current_position = "SalimB"


def javascript(bot, update):
	InlineKeyboard = [
		[InlineKeyboardButton("1-Dars", callback_data="js1"),
		 InlineKeyboardButton("2-Dars", callback_data="js2")],
		[InlineKeyboardButton("3-Dars", callback_data="js3"),
		 InlineKeyboardButton("4-Dars", callback_data="js4")],
		[InlineKeyboardButton("5-Dars", callback_data="js5"),],
		[InlineKeyboardButton("YouTube", url="https://www.youtube.com/playlist?list=PL_WK6W0Gn1I7bL0pRUxYSbTj6g8tHU6Yq"),
		 InlineKeyboardButton("Mover(TAS-IX)", url="https://mover.uz/watch/Cv6hnF8m/?list=kl7W9bfp")]
	]
	reply_markup = InlineKeyboardMarkup(InlineKeyboard)
	update.message.reply_text("Bu darslar Farxod Dadajonov tomonidan tuzilgan va @virtualdars kanalidan olingan!\n"\
							  "Quyidagi darslar ro'yxatidan keraklisini tanlang:", 
		reply_markup=reply_markup)
	global current_position
	current_position = "JavaScript"


def python_darslari(bot, update):
	keyboard = [
		[KeyboardButton("Boshlang'ich Python"),],
		[KeyboardButton("Toshbaqa ilovasi"),],
		[KeyboardButton("Ortga ⬅️"), KeyboardButton("Bosh menyu 🏠")]
	]
	reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
	update.message.reply_text("Kerakli darslarni tanlang:",
							  reply_markup=reply_markup)
	global current_position
	current_position = "Python"


def python_beginner(bot, update):
	InlineKeyboard = [
		[InlineKeyboardButton("1-Dars", callback_data="pb1"),
		 InlineKeyboardButton("2-Dars", callback_data="pb2")],
		[InlineKeyboardButton("3-Dars", callback_data="pb3"),
		 InlineKeyboardButton("4-Dars", callback_data="pb4")],
		[InlineKeyboardButton("5-Dars", callback_data="pb5"),],
		[InlineKeyboardButton("YouTube", url="https://www.youtube.com/playlist?list=PLdNKI0sOr3EVf-ic347ZdJgzzkKCyiror"),
		 InlineKeyboardButton("Mover(TAS-IX)", url="https://mover.uz/watch/42GGJTE/?list=2xkQWLYE")],
		[InlineKeyboardButton("Beruny.uz", url="http://beruny.uz/index.php/kurslar/course/py-beginner")]
	]
	reply_markup = InlineKeyboardMarkup(InlineKeyboard)
	update.message.reply_text("Quyidagi darslar ro'yxatidan keraklisini tanlang:", reply_markup=reply_markup)
	global current_position
	current_position = "PythonB"


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


def broadcast(bot, update):
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


def send_videos(bot, update, link, level, teacher):
	query = update.callback_query
	sending(bot, update)
	bot.send_chat_action(query.message.chat_id, "upload_video")
	bot.send_video(query.message.chat_id,
				   link,
				   caption="{} {}-Dars.\n{}".format(level, query.data[2:], teacher))


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
	elif current_position == "SalimB":
		bot.send_message(chat_id=update.message.chat_id, text="Ortga ⬅️")
		salim_ingliz_tili_darajalari(bot, update)
	elif current_position == "Coding" or current_position == "Langs":
		bot.send_message(chat_id=update.message.chat_id, text="Ortga ⬅️")
		uy(bot, update)
	elif current_position == "JavaScript" or current_position == "Python":
		bot.send_message(chat_id=update.message.chat_id, text="Ortga ⬅️")
		uy(bot, update)
	elif current_position == "PythonB":
		bot.send_message(chat_id=update.message.chat_id, text="Ortga ⬅️")
		python_darslari(bot, update)


def tanlovlar(bot, update):
	msg_txt = update.message.text
	global feedback_id

	if (update.update_id - 1) == feedback_id and msg_txt != "Bekor qilish":
		bot.send_message(chat_id=137786647,
						 text="Hey guys! you've got a feedback!")
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
		salim_ingliz_tili_darajalari(bot, update)
	elif "Beginner 👶" == msg_txt:
		salim_beginner(bot, update)
	elif "Dasturlash kurslari 👨🏻‍💻" == msg_txt:
		dasturlash_kurslari(bot, update)
	elif "JavaScript 🔰" == msg_txt:
		javascript(bot, update)
	elif "Python 🐍" == msg_txt:
		python_darslari(bot, update)
	elif "Boshlang'ich Python" == msg_txt:
		python_beginner(bot, update)
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

	if query.data == "ub1":
		send_videos(bot, update, "https://t.me/BerunyBeginner/14", "Beginner", "Umidjon Sobirov")
	elif query.data == "ub2":
		send_videos(bot, update, "https://t.me/BerunyBeginner/22", "Beginner", "Umidjon Sobirov")
	elif query.data == "ub3":
		send_videos(bot, update, "https://t.me/BerunyBeginner/28", "Beginner", "Umidjon Sobirov")
	elif query.data == "ub4":
		send_videos(bot, update, "https://t.me/BerunyBeginner/42", "Beginner", "Umidjon Sobirov")
	elif query.data == "ub5":
		send_videos(bot, update, "https://t.me/BerunyBeginner/47", "Beginner", "Umidjon Sobirov")
	
	# Query responder for Umid's beginner lessons ends

	"""/////////////////////////////////////////////////////////////////////////////////////"""

	# Query responder for Umid's elementary lessons starts

	if query.data == "ue1":
		send_videos(bot, update, "https://t.me/BerunyBeginner/343", "Elementary", "Umidjon Sobirov")
	elif query.data == "ue2":
		send_videos(bot, update, "https://t.me/BerunyBeginner/354", "Elementary", "Umidjon Sobirov")
	elif query.data == "ue3":
		send_videos(bot, update, "https://t.me/BerunyBeginner/361", "Elementary", "Umidjon Sobirov")
	elif query.data == "ue4":
		send_videos(bot, update, "https://t.me/BerunyBeginner/370", "Elementary", "Umidjon Sobirov")
	elif query.data == "ue5":
		send_videos(bot, update, "https://t.me/BerunyBeginner/376", "Elementary", "Umidjon Sobirov")

	# Query responder for Umid's elementary lessons ends

	"""/////////////////////////////////////////////////////////////////////////////////////"""
	
	# Query responder for my beginner course starts

	if query.data == "tanishuv":
		sending(bot, update)
		bot.send_chat_action(query.message.chat_id, "upload_video")
		bot.send_video(query.message.chat_id,
					   "https://t.me/testberuny/6",
					   caption="Kurs bilan tanishuv.\nShosalim Bakhtiyorov")
	elif query.data == "sb1":
		send_videos(bot, update, "https://t.me/testberuny/7", "Beginner", "Shosalim Bakhtiyorov")
	elif query.data == "sb2":
		send_videos(bot, update, "https://t.me/testberuny/8", "Beginner", "Shosalim Bakhtiyorov")
	elif query.data == "sb3":
		send_videos(bot, update, "https://t.me/testberuny/17", "Beginner", "Shosalim Bakhtiyorov")
	elif query.data == "sb4":
		send_videos(bot, update, "https://t.me/testberuny/16", "Beginner", "Shosalim Bakhtiyorov")
	elif query.data == "sb5":
		send_videos(bot, update, "https://t.me/testberuny/18", "Beginner", "Shosalim Bakhtiyorov")

	# Query responder for my beginner course finishes

	"""/////////////////////////////////////////////////////////////////////////////////////"""

	# Query responder for JS lessons starts

	if query.data == "js1":
		send_videos(bot, update, "https://t.me/virtualdars/165", "JavaScript", "Farxod Dadajonov")
	elif query.data == "js2":
		send_videos(bot, update, "https://t.me/virtualdars/168", "JavaScript", "Farxod Dadajonov")
	elif query.data == "js3":
		send_videos(bot, update, "https://t.me/virtualdars/169", "JavaScript", "Farxod Dadajonov")
	elif query.data == "js4":
		send_videos(bot, update, "https://t.me/virtualdars/170", "JavaScript", "Farxod Dadajonov")
	elif query.data == "js5":
		send_videos(bot, update, "https://t.me/virtualdars/171", "JavaScript", "Farxod Dadajonov")

	# Query for Python Beginner lessons starts

	"""/////////////////////////////////////////////////////////////////////////////////////"""

	if query.data == "pb1":
		send_videos(bot, update, "https://t.me/testberuny/9", "Python Beginner", "Dostonbek Toirov")
	elif query.data == "pb2":
		send_videos(bot, update, "https://t.me/testberuny/10", "Python Beginner", "Dostonbek Toirov")
	elif query.data == "pb3":
		send_videos(bot, update, "https://t.me/testberuny/11", "Python Beginner", "Dostonbek Toirov")
	elif query.data == "pb4":
		send_videos(bot, update, "https://t.me/testberuny/12", "Python Beginner", "Dostonbek Toirov")
	elif query.data == "pb5":
		send_videos(bot, update, "https://t.me/testberuny/13", "Python Beginner", "Dostonbek Toirov")


start_handler = CH('start', start)
broadcast_handler = CH('broadcast', broadcast)
ids_handler = CH('ids', ids)
dper.add_handler(ids_handler)
dper.add_handler(start_handler)
dper.add_handler(broadcast_handler)
dper.add_handler(CQH(darsalar_uchun_query))
dper.add_handler(CH('id', chat_id))
dper.add_handler(MH(Filters.text, tanlovlar))


import os
PORT = os.environ.get('PORT')
uper.start_webhook(listen="0.0.0",
				   port=int(PORT),
				   url_path=token)
uper.bot.setWebhook("https://beruny-bot.herokuapp.com/{}".format(token))
uper.idle()