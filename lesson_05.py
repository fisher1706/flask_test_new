# https://www.youtube.com/watch?v=oM39KVYsjRs&list=PLA0M1Bcd0w8yrxtwgqBvT6OM4HkOU3xYn&index=4

from flask import Flask, render_template, request

app = Flask(__name__)

menu = [{'title': 'Install', 'url': 'install-flask'},
        {'title': 'First application', 'url': 'first-app'},
        {'title': 'Feedback', 'url': 'contact'}]


@app.route("/")
def index():
    return render_template('index.html', menu=menu)


@app.route("/about")
def about():
    return render_template('about.html', title='About Site', menu=menu)


@app.route("/contact", methods=['POST'])
def contact():
    if request.method == 'POST':
        return request.form['name']
        # print(request.form)
        # print(request.form['username'])
        # print(request.form['email'])
        # print(request.form['message'])

    # return render_template('contact.html', title='Feedback', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
