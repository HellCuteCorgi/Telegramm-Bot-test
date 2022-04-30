from enum import Enum

token = "5177477087:AAEGumAhmOG9Sv50yRg2EPZl8aYCrkUr08g" # токен бота
db_file = "database.vdb" # ФСДБ Vedis для обработки стадий MessageHandler
db_server = "HELLCUTECORGI" # Имя SQL сервера
db_database = "tgbot" # Название БД SQL


class States(Enum): # стадии MessageHandler
    S_START = "0"  # Начало нового диалога
    S_DISTRICT = "1"
    S_POLY = "2"
    S_SPEC = "3"
    S_VRADCH = "4"
    S_DATE = "5"
    S_TIME = "6"
    S_POLIS = "7"
    S_NAME = "8"
    S_FINISH = "9"