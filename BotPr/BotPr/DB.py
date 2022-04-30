from vedis import Vedis
import pyodbc
import config


# Пытаемся узнать из базы «состояние» пользователя
def get_current_state(user_id):
    with Vedis(config.db_file) as db:
        try:
            return db[user_id].decode()
        except KeyError:  # Если такого ключа почему-то не оказалось
            return config.States.S_START.value  # значение по умолчанию - начало диалога


# Сохраняем текущее «состояние» пользователя в нашу базу
def set_state(user_id, value):
    with Vedis(config.db_file) as db:
        try:
            db[user_id] = value
            return True
        except:
            # тут желательно как-то обработать ситуацию
            return False

# подружимся с MS SQL Server
conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};""Server="+config.db_server+";""Database="+config.db_database+";""Trusted_Connection=yes;") # инициализируем подключение
cursor = conn.cursor()
cursor.execute("SELECT @@version")
row = cursor.fetchone()
if not row:
    print("Инициализация с БД "+config.db_database+" не пройдена.")
else:
    print("Инициализация с БД "+config.db_database+" пройдена.\nСервер: "+config.db_server)
 