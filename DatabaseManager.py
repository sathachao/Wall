__author__ = 'Satha'

import psycopg2

class DatabaseManager:
    try:

        username = "postgres"
        password = ""

        db = psycopg2.connect(database="Wall", user=username, password=password)
        cur = db.cursor()
        print("Connect successfully")
    except:
        print("Cannot connect to database")

    def __init__(self):
        print("No initialization allowed")

    @staticmethod
    def getCursor():
        return DatabaseManager.cur

    @staticmethod
    def execute(query):
        DatabaseManager.cur.execute(query)

    @staticmethod
    def fetch():
        return DatabaseManager.cur.fetchall()