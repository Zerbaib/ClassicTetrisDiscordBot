import mysql.connector
from src.utils.logger import Log
from src.utils.config import get_config


def connect_db():
    try:
        conn = mysql.connector.connect(
            user=get_config("DB_USER"),
            password=get_config("DB_PASS"),
            host=get_config("DB_HOST"),
            port=get_config("DB_PORT"),
            database=get_config("DB_NAME")
        )
        cur = conn.cursor()
        return cur, conn
    except Exception as e:
        Log.error("Failed to connect to database")
        Log.error(e)
        exit()

class Saver():
    def __init__(self):
        pass

    def fetch(dataTable, presision, dataFetch = "*"):
        """
        Fetch data from the database

        Parameters:
            dataTable (str): The table to fetch data from
            presision (dict): The conditions to fetch data
            dataFetch (list): The data to fetch

        Returns:
            data (list): The fetched data
        """
        try:
            if type(dataFetch) == list:
                dataFetch = ", ".join(dataFetch)
            query = f"SELECT {dataFetch} FROM {dataTable}"
            if presision:
                query += f" WHERE"
                for item in presision:
                    query += f" {item} AND"
                query = query[:-4]
            Log.sql(query)
            return sql_cur_fetchall(query)
        except Exception as e:
            if "list index out of range" in str(e):
                Log.warn(e)
            Log.error("Failed to fetch data")
            Log.error(e)
            return
    def save(dataTable, data):
        """
        Save data to the database

        Parameters:
            dataTable (str): The table to save data to
            data (dict): The data to save

        Returns:
            None
        """
        try:
            query = f"INSERT INTO {dataTable}"
            query += " ("
            for item in data:
                query += f"{item}, "
            query = query[:-2]
            query += ") VALUES ("
            for item in data:
                query += f"{data[item]}, "
            query = query[:-2]
            query += ")"
            Log.sql(query)

            cur, conn = connect_db()
            cur.execute(query)
            conn.commit()
            cur.close()
            conn.close()
        except Exception as e:
            Log.error("Failed to save data")
            Log.error(e)
            return
    def update(dataTable, presision, data):
        """
        Update data in the database
        
        Parameters:
            dataTable (str): The table to update data in
            presision (dict): The conditions to update data
            data (dict): The data to update
        
        Returns:
            None
        """
        try:
            query = f"UPDATE {dataTable} SET"
            for item in data:
                if data[item] == str(data[item]):
                    query += f" {item} = '{data[item]}',"
                else:
                    query += f" {item} = {data[item]},"
            query = query[:-1]
            if presision:
                query += " WHERE"
                for item in presision:
                    query += f" {item} AND"
                query = query[:-4]
            Log.sql(query)

            cur, conn = connect_db()
            cur.execute(query)
            conn.commit()
            cur.close()
            conn.close()
        except Exception as e:
            Log.error("Failed to update data")
            Log.error(e)
            return
    def get_top(dataTable, presision, limit):
        """
        Get the top data from the database

        Parameters:
            dataTable (str): The table to get data from
            presision (dict): The conditions to order data
            limit (int): The amount of data to get

        Returns:
            data (list): The fetched data
        """
        try:
            query = f"SELECT * FROM {dataTable} ORDER BY {presision} DESC LIMIT {limit}"
            Log.sql(query)
            return sql_cur_fetchall(query)
        except Exception as e:
            Log.error("Failed to get top data")
            Log.error(e)
            return
    def query(query):
        """
        Execute a query

        Parameters:
            query (str): The query to execute

        Returns:
            data (list): The fetched data
        """
        try:
            cur, conn = connect_db()
            cur.execute(query)
            data = cur.fetchall()
            conn.commit()
            cur.close()
            conn.close()
            Log.sql(query)

            return data
        except Exception as e:
            Log.error("Failed to execute query")
            Log.error(e)
            return

def sql_cur_fetchall(query):
    cur, conn = connect_db()
    cur.execute(query)
    data = cur.fetchall()
    conn.close()
    return data