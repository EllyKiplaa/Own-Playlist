from flask import render_template
from . import main

#views 
@main.route('/')
@main.route("/home")
def index():
    ''' root page function that renders the index page. '''
    return render_template('index.html')

@main.route("/about")
def about():
    return render_template('about.html', title='About')