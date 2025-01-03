from src.data.var import files
from src.utils.config import get_config
import mysql.connector
from src.utils.logger import Log
from src.utils.saver import connect_db, create_db

with open(files["instructions"], 'r') as f:
    dbInstructions = f.read()

class Executor:
    def __init__(self):
        self.dbUser = get_config("DB_USER")
        self.dbPass = get_config("DB_PASS")
        self.dbHost = get_config("DB_HOST")
        self.dbPort = int(get_config("DB_PORT"))
        self.dbName = get_config("DB_NAME")
        create_db(dbInstructions)