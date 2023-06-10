import sqlite3

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def create_table():
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     username TEXT NOT NULL,
                     password TEXT NOT NULL)''')
        conn.commit()
        conn.close()

    def save(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                  (self.username, self.password))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users")
        rows = c.fetchall()
        conn.close()
        return rows


