from flask import Flask, url_for, request, render_template, make_response, abort, redirect
from markupsafe import escape, Markup
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/')
def index():
    return 'pagina inicial'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

def do_the_login():
    return "Você está logado"

def show_the_login_form():
    return "Formulario de login"

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

'''
https://flask.palletsprojects.com/en/1.1.x/quickstart/
'''