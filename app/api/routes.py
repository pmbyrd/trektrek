import os
from flask import jsonify
from app.api import api
from app.schemas.movie_schema import MovieSchema
from app.models.star_trek_models import Movie

@api.route('/api/test')
def testing():
    """Test request to for json"""
    return jsonify({'test': 'test'})

@api.route('/api/OMDB_API_KEY')
def omdb_api_key():
    """Returns the OMDB_API_KEY"""
    OMDB_API_KEY = os.environ.get('OMDB_API_KEY')
    return jsonify({'OMDB_API_KEY': 'OMDB_API_KEY'})
    
@api.route('/api/TMDB_API_KEY')
def tmdb_api_key():
    """Returns the TMDB_API_KEY"""
    TMDB_API_KEY = os.environ.get('TMDB_API_KEY')
    return jsonify({'TMDB_API_KEY': 'TMDB_API_KEY'})

@api.route('/api/movies')
def json_movies():
    """Returns all movies in the database"""
    movies = MovieSchema(many=True).dump(Movie.query.all())
    return jsonify(movies)