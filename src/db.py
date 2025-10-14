import sqlite3

def get_connection():
    return sqlite3.connect('example.db')

def insert_item(item):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO orders (item) VALUES (?)", (item,))
    conn.commit()

def query_items():
    conn = get_connection()
    cursor = conn.cursor()
    result = cursor.execute("SELECT item FROM orders")
    return [row[0] for row in result]
