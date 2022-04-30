#Тут лежат обработчики действий в SQL и маркапов
import telebot # pyTelegramBotAPI
from telebot import types
import config # config.py
import db # db.py
import BotPr # bot.py

# кнопки выбора районов
db.cursor.execute("SELECT name FROM district")
district = db.cursor.fetchall()
district_m = types.ReplyKeyboardMarkup(resize_keyboard=True)
for i in range(0, len(district)):
    if not district:
        print("sql syntax error on district")
    else:
        district_str = str(district[i])
        district_str = district_str.replace('(','')
        district_str = district_str.replace(')','')
        district_str = district_str.replace(',','')
        district_str = district_str.replace("'",'')
        district_m.add(types.KeyboardButton(district_str))
        print("RAION "+str(i)+" = "+district_str) # тестим вывод

# кнопки выбора поликлиник
def get_poly(d_perm):
    db.cursor.execute("SELECT poly.name_poly FROM poly INNER JOIN district ON poly.id_district = district.id WHERE district.name = ?", (d_perm))
    poly = db.cursor.fetchall()
    poly_m = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(0, len(poly)):
            if not poly:
                print("sql syntax error on poly")
            else:
                poly_str = str(poly[i])
                poly_str = poly_str.replace('(','')
                poly_str = poly_str.replace(')','')
                poly_str = poly_str.replace(',','')
                poly_str = poly_str.replace("'",'')
                poly_m.add(types.KeyboardButton(poly_str))
    return poly_m

# кнопки выбора специлизации
def get_spec():
    db.cursor.execute("SELECT name_spec FROM specialist")
    spec = db.cursor.fetchall()
    spec_m = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(0, len(spec)):
        if not spec:
            print("sql syntax error on spec")
        else:
            spec_str = str(spec[i])
            spec_str = spec_str.replace('(','')
            spec_str = spec_str.replace(')','')
            spec_str = spec_str.replace(',','')
            spec_str = spec_str.replace("'",'')
            spec_m.add(types.KeyboardButton(spec_str))
        return spec_m

# кнопки выбора врача
def get_vradch(s_perm, p_perm):
    db.cursor.execute("SELECT vradch.fio FROM vradch INNER JOIN poly ON poly.id = vradch.id_poly INNER JOIN specialist ON specialist.id = vradch.id_spec WHERE poly.name_poly = ? AND specialist.name_spec = ?", (p_perm,s_perm))
    spec = db.cursor.fetchall()
    spec_m = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(0, len(spec)):
        if not spec:
            print("sql syntax error on spec")
        else:
            spec_str = str(spec[i])
            spec_str = spec_str.replace('(','')
            spec_str = spec_str.replace(')','')
            spec_str = spec_str.replace(',','')
            spec_str = spec_str.replace("'",'')
            spec_m.add(types.KeyboardButton(spec_str))
        return spec_m

# кнопки выбора даты
def get_date(v_perm, p_perm):
    db.cursor.execute("SELECT date FROM talons INNER JOIN vradch ON vradch.id = talons.id_vradch INNER JOIN poly ON poly.id = vradch.id_poly WHERE vradch.fio = ? AND poly.name_poly = ?", (v_perm,p_perm))
    spec = db.cursor.fetchall()
    spec_m = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(0, len(spec)):
        if not spec:
            print("sql syntax error on spec")
        else:
            spec_str = str(spec[i])
            spec_str = spec_str.replace('(','')
            spec_str = spec_str.replace(')','')
            spec_str = spec_str.replace(',','')
            spec_str = spec_str.replace("'",'')
            spec_m.add(types.KeyboardButton(spec_str))
        return spec_m

# кнопки выбора времени
def get_time(v_perm,p_perm,d_perm):    
db.cursor.execute("SELECT time FROM talons INNER JOIN vradch ON vradch.id = talons.id_vradch INNER JOIN poly ON poly.id = vradch.id_poly WHERE vradch.fio = ? AND poly.name_poly = ? AND talons.date = ?", (v_perm,p_perm,d_perm))
    spec = db.cursor.fetchall()
    spec_m = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(0, len(spec)):
        if not spec:
            print("sql syntax error on spec")
        else:
            spec_str = str(spec[i])
            spec_str = spec_str.replace('(','')
            spec_str = spec_str.replace(')','')
            spec_str = spec_str.replace(',','')
            spec_str = spec_str.replace("'",'')
            spec_m.add(types.KeyboardButton(spec_str))
    return spec_m

def check_date(v_perm,p_perm,d_perm):
    db.cursor.execute("SELECT timeRdR FROM talons INNER JOIN vradch ON vradch.id = talons.id_vradch INNER JOIN poly ON poly.id = vradch.id_poly WHERE vradch.fio = ? AND poly.name_poly = ? AND talons.date = ?", (v_perm,p_perm,d_perm))
    spec = db.cursor.fetchall()
    spec_m = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(0, len(spec)):
        if not spec:
            print("sql syntax error on spec")
        else:
            spec_str = str(spec[i])
            spec_str = spec_str.replace('(','')
            spec_str = spec_str.replace(')','')
            spec_str = spec_str.replace(',','')
            spec_str = spec_str.replace("'",'')
            spec_m.add(types.KeyboardButton(spec_str))
            return spec_str

# запись в sql
def insert_db(v_perm,pl_perm,di_perm,s_perm, t_perm, d_perm, p_perm):
    db.cursor.execute("SELECT talons.id FROM talons INNER JOIN vradch ON vradch.id = talons.id_vradch INNER JOIN poly ON poly.id = vradch.id_poly WHERE vradch.fio = ? AND poly.name_poly = ? AND talons.date = ? AND talons.time = ?", (v_perm,pl_perm,d_perm,t_perm))
    idtalon = db.cursor.fetchall();
    idtalon = str(idtalon)
    idtalon = idtalon.replace('(','')
    idtalon = idtalon.replace(')','')
    idtalon = idtalon.replace(',','')
    idtalon = idtalon.replace("'",'')
    print(idtalon)
    db.cursor.execute("INSERT INTO zapisi(polis,district,poly,specialist,vradch) VALUES (?,?,?,?,?)", (pl_perm, di_perm, p_perm,s_perm, v_perm))
    print("+")



print("\n\n\nПроверка прошла успешно. Модули загружены.") # системное уведомление о прохождении
