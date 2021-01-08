from flask import Flask, render_template, redirect, url_for, request, g, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm, Form
from wtforms import StringField, SubmitField, Form, BooleanField, PasswordField, validators
from wtforms.validators import DataRequired
from datetime import datetime
import requests

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '45345FDF-FREEDJHG4-HDGDTER5'
    
    Bootstrap(app)

    return app

app = create_app()

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='Nikola', password='password'))
users.append(User(id=2, username='Luka', password='123'))
users.append(User(id=3, username='Andela', password='321'))
users.append(User(id=4, username='Mateo', password='456'))
users.append(User(id=5, username='Elvis', password='789'))

@app.route('/home')
def index():
    url = 'http://api.openweathermap.org/data/2.5/weather'
    parameters = {'q': 'zadar', 'appid': 'bd62128bfda0efc6224032f105075a21', 'lang':'hr', 'units':'metric'}
    response = requests.get(url, parameters)
    weather = response.json()
    return render_template("index.html", weather = weather, datetime = datetime)

@app.route('/profile')
def indexprofile():
    url = 'http://api.openweathermap.org/data/2.5/weather'
    parameters = {'q': 'zadar', 'appid': 'bd62128bfda0efc6224032f105075a21', 'lang':'hr', 'units':'metric'}
    response = requests.get(url, parameters)
    weather = response.json()
    return render_template("profile.html", weather = weather, datetime = datetime)

@app.route('/')
def indexlogin():
    url = 'http://api.openweathermap.org/data/2.5/weather'
    parameters = {'q': 'zadar', 'appid': 'bd62128bfda0efc6224032f105075a21', 'lang':'hr', 'units':'metric'}
    response = requests.get(url, parameters)
    weather = response.json()
    return render_template("login.html", weather = weather, datetime = datetime)

@app.route('/gallery')
def indexgallery():
    url = 'http://api.openweathermap.org/data/2.5/weather'
    parameters = {'q': 'zadar', 'appid': 'bd62128bfda0efc6224032f105075a21', 'lang':'hr', 'units':'metric'}
    response = requests.get(url, parameters)
    weather = response.json()
    return render_template("gallery.html", weather = weather, datetime = datetime)

@app.route('/guestgallery')
def guestgallery():
    url = 'http://api.openweathermap.org/data/2.5/weather'
    parameters = {'q': 'zadar', 'appid': 'bd62128bfda0efc6224032f105075a21', 'lang':'hr', 'units':'metric'}
    response = requests.get(url, parameters)
    weather = response.json()
    return render_template("guestgallery.html", weather = weather, datetime = datetime)

@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user
        

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('profile'))

        return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/profile')
def profile():
    if not g.user:
        return redirect(url_for('login'))

    return render_template('profile.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')
