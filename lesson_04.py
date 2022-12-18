# https://www.youtube.com/watch?v=oM39KVYsjRs&list=PLA0M1Bcd0w8yrxtwgqBvT6OM4HkOU3xYn&index=4

from flask import Flask, render_template, url_for

app = Flask(__name__)

menu = ['Install', 'First application', 'Feedback']


@app.route("/")
def index():
    print(url_for('index'))
    return render_template('index.html', menu=menu)


@app.route("/about")
def about():
    print(url_for('about'))
    return render_template('about.html', title='About Site', menu=menu)


# @app.route("/profile/<username>")
# @app.route("/profile/<path:username>")
@app.route("/profile/<int:username>/<path>")
# def profile(username):
def profile(username, path):
    # return f'User: {username}'
    return f'User: {username}, {path}'


with app.test_request_context():
    print(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
