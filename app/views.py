from flask import render_template, request, redirect, url_for, session, flash
from app import app
from app.model.user_model import User
from app.model.application import Application
from app.model.shopping_model import Shopping, Shopping_list_item


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
                    session.pop('flashes', None)
                    flash("You have successfully signed up. Please Login")
                    return redirect(url_for('login'))
                return render_template('index.html', error='Known \
                                       credetials! proceed to login')
            error = 'Passwords do not match'
            return render_template('index.html', error=error)
    return render_template('index.html', error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_error = None
    if request.method == 'POST':
        if request.form['username'] and request.form['password']:
            if application.does_user_exist(request.form['username']):
                if application.login_user(request.form['username'],
                                          request.form['password']):
                    session['username'] = request.form['username']
                    return redirect(url_for('shopping_list'))
                return render_template('index.html', login_error='Incorrect \
                                       password')
            return render_template('index.html', login_error='No account \
                                   found, please sign up first')
        login_error = "Invalid credentials, try again"
    return render_template('index.html', login_error=login_error)


@app.route('/shopping_list', methods=['GET', 'POST'])
def shopping_list():
    shopping_error = None
    user = application.get_user(session['username'])
    if not user:
        return redirect(url_for('login'))
    session.pop('flashes', None)
    flash("you have successfully logged in")
    return render_template('profile.html', shopping_error=shopping_error,
                           user=user)


@app.route('/add_shopping_list', methods=['GET', 'POST'])
def add_shopping_list():
    add_error = None
    user = application.get_user(session['username'])
    print ">>>", user
    if not user:
        return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form['name']
        shopping_list_id = application.generate_random_key()
        if user.create_shopping_list(Shopping(
            shopping_list_id, name)):
            print "kawa"
            items_list = request.form['items'].split('--')
            shop = user.get_shopping_list(shopping_list_id)
            if shop.create_item(
                    Shopping_list_item(application.generate_random_key(),
                                       "", items_list,
                                       request.form['due'])):
                flash("The shopping list has succeefully been added")
                return redirect(url_for('shopping_list_feed'))
        add_error = "The shopping list exists already"
    session.pop('flashes', None)
    #flash("")
    return render_template('add_shopping_list.html',
                           add_error=add_error, user=user)


@app.route('/shopping_list_feed', methods=['GET', 'POST'])
def shopping_list_feed():
    feed_error = None
    user = application.get_user(session['username'])
    if not user:
        return redirect(url_for('login'))
    return render_template('index_feed.html', user=user,
                           shopping_lists=user.get_all_shopping_lists(),
                           feed_error=feed_error)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))
