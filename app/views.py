from flask import render_template, request, redirect, url_for, session, flash
from app import app
from app.model.user_model import User
from app.model.application import Application
from app.model.shopping_model import Shopping, Shopping_list_item


application = Application()


def get_user_items(shopping_lists):
    shopping_lists_with_items = dict
    print shopping_lists
    for list_key, list_value in shopping_lists.items():
        list_name = list_value.name
        items = list_value.shopping_list.values()
        for item in items:
            print item
            shopping_lists_with_items[list_name] = {'items':item.description,
                                                  'date':item.deadline}
    return shopping_lists_with_items


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
                    flash("you have successfully logged in", 'login_success')
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

    shopping_lists_with_items = dict()
    shopping_lists = user.get_all_shopping_lists()
    for list_key, list_value in shopping_lists.items():
        list_name = list_value.name
        items = list_value.shopping_list.values()
        for item in items:
            shopping_lists_with_items[list_name] = {'items':item.description,
                                                  'date':item.deadline,
                                                    'shop_id':list_key,
                                                    'shop_id_list':item.id}

    return render_template('profile.html', shopping_error=shopping_error,
                           shopping_lists=shopping_lists_with_items,
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
            shop = user.get_shopping_list(shopping_list_id)
            if shop.create_item(
                    Shopping_list_item(application.generate_random_key(),
                                       "", request.form['items'],
                                       request.form['due'])):
                flash("The shopping list has succeefully been added", )
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

    #shopping_lists_with_items = get_user_items(user.get_all_shopping_lists())

    shopping_lists_with_items = dict()
    shopping_lists = user.get_all_shopping_lists()
    for list_key, list_value in shopping_lists.items():
        list_name = list_value.name
        items = list_value.shopping_list.values()
        for item in items:
            shopping_lists_with_items[list_name] = {'items':item.description,
                                                  'date':item.deadline}
    return render_template('index_feed.html', user=user,
                           shopping_lists=shopping_lists_with_items,
                           feed_error=feed_error)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/delete/shopping_list/<list_id>', methods=['GET', 'POST'])
def delete_shopping_list(list_id):
    error = None
    user = application.get_user(session['username'])
    if not user:
        return redirect(url_for('login'))
    shopping_list = user.get_shopping_list(list_id)
    if not shopping_list:
        flash("Success fully deleted ", "deleted")
        return redirect(url_for('shopping_list'))

    shopping_lists_with_items = dict()
    shopping_lists = user.get_all_shopping_lists()
    for list_key, list_value in shopping_lists.items():
        list_name = list_value.name
        items = list_value.shopping_list.values()
        for item in items:
            shopping_lists_with_items[list_name] = {'items':item.description,
                                                  'date':item.deadline}

    if request.method == 'GET':
        if user.delete_shopping_list(list_id):
            flash("You have successfully Deleted the shopping list")
            return redirect(url_for('shopping_list'))
        error = "Could not delete the specified shopping list"
    return render_template('profile.html', error=error,
                           shopping_lists=shopping_lists_with_items,
                           user=user)



@app.route('/update', methods=['GET', 'POST'])
def update_shopping_list():
    if request.form['shopping_id'] and request.form['list_id']:
        shopping_id = request.form['shopping_id']
        list_id = request.form['list_id']
    print ">>>>>", shopping_id, list_id
    error = None
    user = application.get_user(session['username'])
    if not user:
        return redirect(url_for('login'))
    shopping_list = user.get_shopping_list(shopping_id)
    if not shopping_list:
        return redirect(url_for('shopping_list'))

    if request.method == 'POST':
        name = request.form['name']
        if name:
            if user.update_shopping_list(shopping_id, name):
                if shopping_list.update_item(list_id, request.form['name'],
                                      request.form['items'],
                                      request.form['due-date']):
                    flash("You have successfully updated your Bucket")
                    return redirect(url_for('shopping_list'))
        error = "Please provide the bucket name"

    shopping_lists_with_items = dict()
    shopping_lists = user.get_all_shopping_lists()
    for list_key, list_value in shopping_lists.items():
        list_name = list_value.name
        items = list_value.shopping_list.values()
        for item in items:
            shopping_lists_with_items[list_name] = {'items':item.description,
                                                  'date':item.deadline}

    return render_template('profile.html', error=error,
                           shopping_lists=shopping_lists_with_items,
                           user=user)

