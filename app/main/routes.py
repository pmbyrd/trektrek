from app.main import bp as main
from flask import render_template, url_for, flash, redirect, request, session, jsonify
from app.models.search import Search
from app.models.star_trek_models import Character
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


@main.route('/')
def index():
    return render_template('index.html', title='Home')
    
    
@main.route('/profile')
def profile():
    if session["user"]:
        user = session["user"]
        return render_template('profile.html', user=user)
    else:
        return redirect(url_for('auth.login'))
    
@main.route('/test/')
def test_page():
   return '<h1>Testing the Flask Application Factory Pattern</h1>'

@main.route('/map')
def map():
    return render_template('map.html')
    
    
