from app.main import bp as main
from flask import render_template, url_for, flash, redirect, request, Blueprint



@main.route('/')
def index():
    return render_template('index.html')    

@main.route('/test/')
def test_page():
   return '<h1>Testing the Flask Application Factory Pattern</h1>'
    
    
