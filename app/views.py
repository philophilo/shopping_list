from flask import render_template, request, redirect, url_for, session, flash
from app import app
from app.model.user_model import User
from app.model.application import Application


application = Application()


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        if request.form['name'] and request.form['username'] and \
                    request.form['password'] and \
                    request.form['confirm-password']:

            if request.form['password'] == request.form['confirm-password']:
                user = User(request.form['username'],
                            request.form['password'],
                            request.form['name'])
                if application.register_user(user):
                    flash("You have successfully signed up. Please Login")
                    return redirect(url_for('login'))
                return render_template('index.html', error=
                                       'Known credetials! proceed to login')
            error = 'Passwords do not match'
            return render_template('index.html', error=error)
    return render_template('index.html', error=error)

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_error = None
    if request.method == 'POST':
        if request.form['username'] and request.form['password']:
            print "\ncheck username and password\n"
            print application.does_user_exist(request.form['username'])
            if application.does_user_exist(request.form['username']):
                print "\ncheck if user exists\n"
                if application.login_user(request.form['username'], \
                                              request.form['password']):
                    print "\nlogin user\n"
                    session['username'] = request.form['username']
                    return redirect(url_for('shopping_list'))
                return render_template('index.html', login_error=
                                   'Incorrect password')
            return render_template('index.html', login_error=
                               'No account found, please sign up first')
        error = "Invalid credentials, try again"
    return render_template('index.html', login_error=login_error)

@app.route('/shopping_list', methods=['GET', 'POST'])
def shopping_list():
    shopping_error = None
    user = application.get_user(session['username'])
    if not user:
        print None
        return redirect(url_for('login'))
    else:
        name = request.form['name']
        return redirect(url_for('bucketlist'), name=name)
    return render_template('index.html', shopping_error=shopping_error)
