import sqlite3

class DbHelper:
    def query(self, sql):
        conn = sqlite3.connect("test.db")
        cursor = conn.cursor()
        result = cursor.execute(sql)
        return result  

    def update(self, sql):
        conn = sqlite3.connect("test.db")
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
