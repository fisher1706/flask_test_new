# https://www.youtube.com/watch?v=b-Pi5Ggnm2w&list=PLA0M1Bcd0w8yrxtwgqBvT6OM4HkOU3xYn&index=6

from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'zapel'


menu = [{'title': 'Install', 'url': 'install-flask'},
        {'title': 'First application', 'url': 'first-app'},
        {'title': 'Feedback', 'url': 'contact'}]


@app.route("/")
def index():
    return render_template('index.html', menu=menu)


@app.route("/about")
def about():
    return render_template('about.html', title='About Site', menu=menu)


@app.route("/contact", methods=['POST', 'GET'])
def contact():

    if request.method == 'POST':
        print(request.form)

        if len(request.form['message']) > 2:
            flash('Message sent', category='success')
        else:
            flash('Error', category='error')

    return render_template('contact.html', title='Feedback', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
