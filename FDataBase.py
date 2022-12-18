import sqlite3
import time
import math
import re
from flask import url_for


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getMenu(self):
        sql = '''SELECT * FROM mainmenu'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except:
            print('Error read from DB')
        return []

    def addPost(self, title, text, url):
        try:
            self.__cur.execute(f"SELECT COUNT() as 'count' FROM posts WHERE url LIKE '{url}'")
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print('Articles with such url already exists')
                return False

            base = url_for('static', filename='images.html')
            text = re.sub(r"(?P<tag><img\s+[^>]*src=)(?P<quote>[\"'])(?P<url>.+?)(?P=quote)>",
                          "\\g<tag>" + base + "/\\g<url>>", text)

            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO posts VALUES (NULL, ?, ?, ?, ?)", (title, text, url, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print(f'Error add article in DB {str(e)}')
            return False
        return True

    def getPost(self, alias):
        try:
            sql = f"SELECT title, text FROM posts WHERE url LIKE '{alias}'"
            self.__cur.execute(sql)
            res = self.__cur.fetchone()
            if res:
                print(res)
                return res
        except sqlite3.Error as e:
            print(f'Error get article from DB {str(e)}')

        return False, False

    def getPostsAnonce(self):
        try:
            sql = f"SELECT id, title, url, text FROM posts ORDER BY time DESC"
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print(f'Error get articles from DB {str(e)}')
        return []

    def addUser(self, name, email, hpsw):
        try:
            self.__cur.execute(f"SELECT COUNT() as 'count' FROM users WHERE email LIKE '{email}'")
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print('There is user with such email')
                return False
            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO users VALUES(NULL, ?, ?, ?, NULL, ?)", (name, email, hpsw, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print(f'Error get user from DB {str(e)}')
            return False
        return True

    def getUser(self, user_id):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE id = {user_id}")
            res = self.__cur.fetchone()
            if not res:
                print('User not found')
                return False
            return res
        except sqlite3.Error as e:
            print(f'Error get data user from DB {str(e)}')
        return False

    def getUserByEmail(self, email):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE email = '{email}' LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print('User not found')
                return False
            return res
        except sqlite3.Error as e:
            print(f'Error get data user from DB {str(e)}')
        return False

    def updateUserAvatar(self, avatar, user_id):
        if not avatar:
            return False
        try:
            binary = sqlite3.Binary(avatar)
            self.__cur.execute(f"UPDATE users SET avatar = ? WHERE id = ?", (binary, user_id))
            self.__db.commit()
        except sqlite3.Error as e:
            print(f'Error update avatar to DB {str(e)}')
            return False
        return True




