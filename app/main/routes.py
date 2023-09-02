from app.main import bp as main
from flask import render_template, url_for, flash, redirect, request, session, jsonify
from app import db
from app.models.star_trek_models import Character
from app.schemas.character_schema import CharacterSchema




@main.route('/')
def index():
    return render_template('index.html', title='Home')
    
@main.route('/search')
def search():
    """A route to search for characters in the database. Jsonify is used to return a json object to the client."""
    # search = request.args["search"]
    # print(search)
    search = request.form['search']
    # print(search)
    choices = request.form.getlist('choices')
    print(choices)
    # get the choice from the form
    # the query can be seen not to use it with the search class
    # data = Character.query.filter(or_(Character.name.ilike(f'%{"data"}%')).all())
    # Ue SQLAlchemy's filter method with the like operator
    characters = Character.query.filter(Character.name.ilike(f"%{search}%")).all()
    data = CharacterSchema(many=True).dump(characters)
    
    # print(data)
    print(characters)
    return jsonify({"results": search,
                "status": 200,
                "data": data})
   
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
    
    
