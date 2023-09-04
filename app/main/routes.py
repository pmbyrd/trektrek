from app.main import bp as main
from flask import render_template, url_for, flash, redirect, request, session, jsonify
from app import db
from app.models.star_trek_models import Character, Performer
from app.schemas.schemas import CharacterSchema, PerformerSchema




@main.route('/')
def index():
    return render_template('index.html', title='Home')

@main.route('/search-post', methods=['POST'])
def search_post():
    """Gets the post request from the front end and responds with a json object."""
    # first try a test to see if the route works
    results = []
    data = request.get_json()
    # break down the data into the search and the choices
    # Access the list element (which is a dictionary)
    res = list(data.values())
    data_list = list(res)[0]
    # Access the keys within the dictionary
    search_key = data_list["search"]
    field_key = data_list["field"]
    if field_key == "characters":
        characters = Character.query.filter(Character.name.ilike(f"%{search_key}%")).all()
        results = [CharacterSchema(many=True).dump(characters)]
        print(results)
        
    if field_key == "performers":
        performers = Performer.query.filter(Performer.name.ilike(f"%{search_key}%")).all()
        results = [PerformerSchema(many=True).dump(performers)]
    
    
    return jsonify({
        "data": "This is a test",
        "results": results,
        "status": 200,
        "message": "This is a test message",
        "field": field_key,
        "search": search_key,
    })
    

   
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
    
    
