from flask import render_template
from app import app

#views 
@app.route('/')
@app.route("/home")
def index():
    ''' root page function that renders the index page. '''
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html', title='About')