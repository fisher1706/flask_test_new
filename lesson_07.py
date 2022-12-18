# https://www.youtube.com/watch?v=QCQ7GDhr4Tc&list=PLA0M1Bcd0w8yrxtwgqBvT6OM4HkOU3xYn&index=7

from flask import Flask, render_template, request, flash, session, redirect, url_for, abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'zapel'


menu = [{'name': 'Install', 'url': 'install-flask'},
        {'name': 'First application', 'url': 'first-app'},
        {'name': 'Feedback', 'url': 'contact'}]


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


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title='Page not found', menu=menu), 404


@app.route('/profile/<username>')
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return f'User profile: {username}'


@app.route("/login", methods=['POST', 'GET'])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'zapel' and request.form['psw'] == '123':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('login.html', title='Authorization', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
