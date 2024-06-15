from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')
@app.route('/generic')
def generic():
    return render_template('generic.html')
@app.route('/elements')
def elements():
    return render_template('elements.html')