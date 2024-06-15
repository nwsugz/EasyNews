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
@app.route('/article_rate/2')
def rate():
    return render_template('article_rate.html')
@app.route('/')
@app.route('/article_rate/2/low')
def low_level():
    return render_template('level_ha.html')
@app.route('/')
@app.route('/article_rate/2/medium')
def medium_level():
    return render_template('level_joong.html')
@app.route('/')
@app.route('/article_rate/2/high')
def high_level():
    return render_template('level_sang.html')