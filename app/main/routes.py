from app.main import bp as main
from flask import render_template, url_for, flash, redirect, request, session, jsonify
from app.models.search import Search
from app.models.star_trek_models import Character



@main.route('/')
def index():
    return render_template('index.html', title='Home')
    
@main.route('/search')
def search():
    """A route to search for characters in the database. Jsonify is used to return a json object to the client."""
    # search = request.args["search"]
    # print(search)
    x = request.args["search"]
    print(x)
    # import pdb; pdb.set_trace()
    return jsonify({"search": x})
    # if request.method == 'POST':
    #     query = request.form['query']
    #     search = Search(query)
    #     results = search.search()
    #     return jsonify(results)
     
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
    
    
