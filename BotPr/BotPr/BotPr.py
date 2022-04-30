import telebot # pyTelegramBotAPI
from telebot import types
import config # config.py
from BotPr import db
import markups # markups.py 

bot = telebot.TeleBot(config.token)

# используем глобальные переменные
di_perm = "" # district
p_perm = "" # poly 
s_perm = "" # spec
v_perm = "" # vradch
d_perm = "" # date
t_perm = "" # time
pl_perm = "" # polis
n_perm = "" # name
uid = "" # message.from_user.username

# действия по кмд /start
# узнаем район
@bot.message_handler(commands=['start'])
def welcome(message):
	state = db.get_current_state(message.chat.id)
	if state == config.States.S_SPEC.value:
		bot.send_message(message.chat.id, "⁉️ <b>Кажется, вы остановились на выборе специалиста.</b> \nВыберите нужного вам специалиста или вернитесь в начало командой /reset".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=None)
	else:
		bot.send_message(message.chat.id, "Добро пожаловать, <b>{0.first_name}</b>!\nДанный бот позволяет записаться к врачу.".format(message.from_user, bot.get_me()),parse_mode='html')
		bot.send_message(message.chat.id, "🧭 Введите район:".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markups.district_m)
		db.set_state(message.chat.id, config.States.S_POLY.value)

# действия по кмд /reset
@bot.message_handler(commands=["reset"])
def cmd_reset(message):
    bot.send_message(message.chat.id, "🧭 Введите район:", reply_markup=markups.district_m)
    db.set_state(message.chat.id, config.States.S_POLY.value)

#действия по кмд /show_rec
@bot.message_handler(commands=["show_rec"])
def cmd_check(message):
    bot.send_message(message.chat.id, "🔎 Ищю ваши записи...Полис №: "+str(pl_perm)+"\n"+str(n_perm)+" простите, но у нас все сломалось :(")
    db.set_state(message.chat.id, config.States.S_POLY.value)

# узнаем поликлинику
@bot.message_handler(func=lambda message: db.get_current_state(message.chat.id) == config.States.S_POLY.value)
def step_district(message):
	global di_perm
	p_district = str(message.text)
	di_perm = p_district
	while True:
		if any(element in p_district for element in markups.district_str):
			bot.send_message(message.chat.id, "🏥 <b>Выберите поликлинику</b>".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markups.get_poly(di_perm))
			db.set_state(message.chat.id, config.States.S_SPEC.value)
			return True
		else:
			bot.send_message(message.chat.id, "😔 Вы ввели неккоректное значение. \n<b>Пожалуйста, введите заного.</b>".format(message.from_user, bot.get_me()),parse_mode='html')
			return False

# узнаем специализацию
@bot.message_handler(func=lambda message: db.get_current_state(message.chat.id) == config.States.S_SPEC.value)
def step_poly(message):
	global p_perm
	poly = str(message.text)
	p_perm = poly
	while True:
		if any(element in poly for element in markups.district_str):			
			bot.send_message(message.chat.id, "<b>Выберите специализацию</b>".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markups.get_spec())
			db.set_state(message.chat.id, config.States.S_VRADCH.value)
			return True
		else:
			bot.send_message(message.chat.id, "😔 Вы ввели неккоректное значение. \n<b>Пожалуйста, введите заного.</b>".format(message.from_user, bot.get_me()),parse_mode='html')
			return False

# узнаем врача
@bot.message_handler(func=lambda message: db.get_current_state(message.chat.id) == config.States.S_VRADCH.value)
def step_vradch(message):
	global s_perm
	global p_perm
	spec = str(message.text)
	s_perm = spec
	while True:
		if any(element in spec for element in markups.district_str):
			bot.send_message(message.chat.id, "💊 <b>Выберите врача</b>".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markups.get_vradch(s_perm, p_perm))
			db.set_state(message.chat.id, config.States.S_DATE.value)
			return True
		else:
			bot.send_message(message.chat.id, "😔 Вы ввели неккоректное значение. \n<b>Пожалуйста, введите заного.</b>".format(message.from_user, bot.get_me()),parse_mode='html')
			return False

# узнаем дату
@bot.message_handler(func=lambda message: db.get_current_state(message.chat.id) == config.States.S_DATE.value)
def step_vradch(message):
	global v_perm
	global p_perm
	vradch = str(message.text)
	v_perm = vradch
	while True:
		if any(element in vradch for element in markups.district_str):
			bot.send_message(message.chat.id, "📆 <b>Выберите дату</b>".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markups.get_date(v_perm, p_perm))
			db.set_state(message.chat.id, config.States.S_TIME.value)
			return True
		else:
			bot.send_message(message.chat.id, "😔 Вы ввели неккоректное значение. \n<b>Пожалуйста, введите заного.</b>".format(message.from_user, bot.get_me()),parse_mode='html')
			return False

# узнаем время
@bot.message_handler(func=lambda message: db.get_current_state(message.chat.id) == config.States.S_TIME.value)
def step_date(message):
	global v_perm
	global p_perm
	global d_perm
	date = str(message.text)
	d_perm = date
	bot.send_message(message.chat.id, "⏰ <b>Выберите время</b>".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markups.get_time(v_perm,p_perm,d_perm))
	db.set_state(message.chat.id, config.States.S_POLIS.value)

# узнаем полис
@bot.message_handler(func=lambda message: db.get_current_state(message.chat.id) == config.States.S_POLIS.value)
def step_time(message):
	global t_perm
	time = str(message.text)
	t_perm = time
	bot.send_message(message.chat.id, "📝 <b>Введите номер полиса</b>".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=None)
	db.set_state(message.chat.id, config.States.S_NAME.value)


@bot.message_handler(func=lambda message: db.get_current_state(message.chat.id) == config.States.S_NAME.value)
def step_polis(message):
	global pl_perm
	polis = str(message.text)
	pl_perm = polis
	while True:
		try:
			polis = int(message.text)
		except ValueError:
			bot.send_message(message.chat.id, "😔 Вы ввели неккоректное число. \n<b>Пожалуйста, введите заного.</b>".format(message.from_user, bot.get_me()),parse_mode='html')
			return False
		else:
			bot.send_message(message.chat.id, "🙃 Великолепно! Введите свое имя, чтобы я в будущем знал как к вам обращаться".format(message.from_user, bot.get_me()),parse_mode='html')
			db.set_state(message.chat.id, config.States.S_FINISH.value)			
			return True

@bot.message_handler(func=lambda message: db.get_current_state(message.chat.id) == config.States.S_FINISH.value)
def nameusr(message):
	while True:
			try:
				global n_perm
				global d_perm 
				global p_perm 
				global s_perm 
				global v_perm 
				global t_perm 
				global pl_perm
				global uid
				name = str(message.text)
				n_perm = name
			except ValueError:
				bot.send_message(message.chat.id, "😔 Вы неккоректно ввели имя! \n<b>Пожалуйста, введите заного.</b>".format(message.from_user, bot.get_me()),parse_mode='html')
				return False
			else:
				bot.send_message(message.chat.id, "👌 "+str(n_perm)+"! Давайте я перечислю что у нас получилось".format(message.from_user, bot.get_me()),parse_mode='html')
				bot.send_message(message.chat.id, "<b>Вы записаны в поликлинику </b>"+str(p_perm)+" "+str(di_perm)+" район"+"\n<b>К специалисту: </b>"+str(s_perm)+"\n<b>Врача зовут: </b>"+str(v_perm)+"\n<b>Дата: </b>"+str(d_perm)+"\n<b>Время: </b>"+str(t_perm)+"\n<b>По полису № </b>"+str(pl_perm)+"".format(message.from_user, bot.get_me()),parse_mode='html')
				bot.send_message(message.chat.id, "👋 До скорой встречи! <b>А что-бы записаться ещё раз, выполните команду /reset, для просмотра записей выполните команду /show_rec</b>".format(message.from_user, bot.get_me()),parse_mode='html')
				name_usr_on_tg = message.from_user.first_name # считываем ник
				uid = message.from_user.username # считываем логин
				print("User: "+name_usr_on_tg+" (@"+uid+") дошел до последнего этапа. Запись сохранена.") # выводим в консоль сообщение о прохождении
				markups.insert_db(v_perm,pl_perm,di_perm,s_perm, t_perm, d_perm, p_perm)
				return True



if __name__ == "__main__":
	bot.infinity_polling()