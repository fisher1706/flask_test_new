# https://www.youtube.com/watch?v=6jxveKOdyNg&list=PLA0M1Bcd0w8yrxtwgqBvT6OM4HkOU3xYn&index=1

from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return "index"


@app.route("/about")
def about():
    return "<h1> about </h1>"


if __name__ == '__main__':
    app.run(debug=True)
