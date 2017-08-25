# shopping_list
<a href="https://codeclimate.com/github/codeclimate/codeclimate/coverage"><img src="https://codeclimate.com/github/codeclimate/codeclimate/badges/coverage.svg" /></a> [![Build Status](https://travis-ci.org/philophilo/shopping_list.svg?branch=master)](https://travis-ci.org/philophilo/shopping_list) [![Coverage Status](https://coveralls.io/repos/philophilo/shopping_list/badge.svg?branch=master)](https://coveralls.io/r/philophilo/shopping_list?branch=master)

This is a shopping list application for the andela bootcamp project. The application allows users to set up their shopping lists.

The project is tracked at
https://www.pivotaltracker.com/projects/2092667

The following are the features

- A user can Register
- A user can Login with specified username and password

__Setup__

To start clone the repository

```
git clone https://github.com/philophilo/shopping_list.git
cd shopping_list
```

Create a virtual environment and activate it

```
virtualenv env
source env/bin/activate
```

Install all the requirements 

```
pip install -r requirements.txt
```

You can now run the application

```
python run.py
```

In the browser

```
http://127.0.0.1:5000
```

You can then run the application tests using

```
cd shopping_list/tests
nosetests -v <testfile>
```
