# https://www.youtube.com/watch?v=b-Pi5Ggnm2w&list=PLA0M1Bcd0w8yrxtwgqBvT6OM4HkOU3xYn&index=13
import os
import datetime
from flask import Flask, session

app = Flask(__name__)

key = os.urandom(20).hex()
print(f'key={key}')

app.config['SECRET_KEY'] = key
app.permanent_session_lifetime = datetime.timedelta(days=10)


@app.route("/")
def index():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1
    return f"<h1>Main page</h><p>Number of views: {session['visits']}"


data = [1, 2, 3, 4]


@app.route("/session")
def session_data():
    session.permanent = True
    if 'data' not in session:
        session['data'] = data
    else:
        session['data'][1] += 1
        session.modified = True

    return f"<p>session['data']: {session['data']}"


if __name__ == '__main__':
    app.run(debug=True)
