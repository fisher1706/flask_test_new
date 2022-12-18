# https://www.youtube.com/watch?v=aHWQkbk3xVA&list=PLA0M1Bcd0w8yrxtwgqBvT6OM4HkOU3xYn&index=8

import sqlite3
import os
from flask import Flask, render_template, g

# configuration
# DATABASE = '/tmp/flsite.db'
# DEBUG = True
# SECRET_KEY = 'zapel1706'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
        db.commit()
        db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route("/")
def index():
    db = get_db()
    return render_template('index.html', menu=[])


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == '__main__':
    # app.run(debug=True)

    # print(dict(DATA=123))
    # print(app.root_path)
    # for i in app.config:
    #     print(i)
    #
    # print(app.config['DATABASE'])

    create_db()
