import sqlite3 as sql
import hashlib

class database():
    def __init__(self):
        self.conn = sql.connect(database="database.db")

    def create_db_tabels(self):
        conn = self.conn
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, fullname TEXT, level INTEGER)")     

        cur.execute("CREATE TABLE IF NOT EXISTS customer (id INTEGER PRIMARY KEY, name TEXT, total INTEGER)")

        cur.execute("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT, description TEXT, costIncl INTEGER)")

        cur.execute("CREATE TABLE IF NOT EXISTS order_items (id INTEGER PRIMARY KEY, user Integer, customer Integer, item Integer, quantity INTEGER)")
        conn.commit()

    def hash_password(self, password):
        hash_object = hashlib.md5(bytes(str(password), encoding='utf-8'))
        return hash_object.hexdigest()

    def create_admin_user(self, password):
        conn = self.conn
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = ?", ('admin',))
        admin = cur.fetchone()
        if (admin == None):
            cur.execute("INSERT INTO users (username, password, fullname, level) VALUES (?, ?, ?, ?)", ('admin', self.hash_password(password), "Administrator", 0))
            conn.commit() 

    def insert_user(self, username, password, fullname, level):
        conn = self.conn
        cur = conn.cursor()
        if level == None: level = 1
        cur.execute("INSERT INTO users (username, password, fullname, level) VALUES (?, ?, ?, ?)", (username, self.hash_password(password), fullname, level))
        resp = conn.commit()
        return 200

    def auth_user(self, username, password):
        conn = self.conn
        cur = conn.cursor()
        try:
            cur.execute("SELECT id, username, fullname, level FROM users WHERE username = ? AND password = ?", (username, self.hash_password(password)))
            resp = cur.fetchone()
            if (resp.__len__() > 0):
                user = {'status': 200, 'user': {id: resp[0], 'username': resp[1], 'fullname': resp[2], 'level': resp[3]}}   
                return user
            else:        
                return {'status': 401}
        except Exception as e:
            return {'status': 401}


