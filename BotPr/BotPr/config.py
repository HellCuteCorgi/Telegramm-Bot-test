from enum import Enum

token = "5177477087:AAEGumAhmOG9Sv50yRg2EPZl8aYCrkUr08g" # ����� ����
db_file = "database.vdb" # ���� Vedis ��� ��������� ������ MessageHandler
db_server = "HELLCUTECORGI" # ��� SQL �������
db_database = "tgbot" # �������� �� SQL


class States(Enum): # ������ MessageHandler
    S_START = "0"  # ������ ������ �������
    S_DISTRICT = "1"
    S_POLY = "2"
    S_SPEC = "3"
    S_VRADCH = "4"
    S_DATE = "5"
    S_TIME = "6"
    S_POLIS = "7"
    S_NAME = "8"
    S_FINISH = "9"