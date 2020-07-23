from flask import Flask
from app import views
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
      
    #Initializing Flask Extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
