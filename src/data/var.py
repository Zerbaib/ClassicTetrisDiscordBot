folders = {
    "config": "./config/",
    "logs": "./logs/",
    "cogs": "./src/modules/",
    "events": "./src/events/"
}

files = {
    "config": f"{folders['config']}config.json"
}

configDataDefault = {
    "TOKEN": "0AZERTYUIOP123QSDFGHJKLM465WXCVBN789",
    "PREFIX": "!",
    "OWNER_ID": "0123456789",
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