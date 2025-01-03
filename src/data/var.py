folders = {
    "config": "./config/",
    "logs": "./logs/"
}

files = {
    "config": f"{folders['config']}config.json"
}

configDataDefault = {
    "TOKEN": "0AZERTYUIOP123QSDFGHJKLM465WXCVBN789",
    "PREFIX": "!",
    "DB_HOST": "localhost",
    "DB_PORT": "3306",
    "DB_USER": "root",
    "DB_PASS": "",
    "DB_NAME": "db_name"
}

def init_time(value):
    global startTimestamp
    global logFile
    startTimestamp = value.strftime("%Hh%M_%d-%m-%Y")
    logFile = f"{folders['logs']}{startTimestamp}.log"

class Color:
    reset = "\033[0m"
    red = "\033[31m"
    orange = "\033[33m"
    green = "\033[32m"
    blue = "\033[34m"