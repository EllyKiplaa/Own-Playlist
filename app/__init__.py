from flask import Flask
from flask_bootstrap import Bootstrap

# Initializing application
app = Flask(__name__)


# Setting up configuration


# Initializing Flask Extensions
bootstrap = Bootstrap(app)

from app import views