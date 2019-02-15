from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'c6b197aed6524cf567357ddaba9e0566'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'trippinapplication@gmail.com'
app.config['MAIL_PASSWORD'] = 'sifra123'
mail = Mail(app)


from flaskapp.users.routes import users
from flaskapp.posts.routes import posts
from flaskapp.main.routes import main


app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
