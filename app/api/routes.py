import os
from dotenv import load_dotenv
from flask import jsonify
from app.api import api
from app.schemas import (
    MovieSchema, 
    SeriesSchema,
    TagSchema,
    CharacterSchema
)
from app.models.star_trek_models import Movie, Series, Character
from app.models.models import Tag

load_dotenv()

@api.route('/api/test')
def testing():
    """Test request to for json"""
    return jsonify({'test': 'test'})

@api.route('/api/OMDB_API_KEY')
def omdb_api_key():
    """Returns the OMDB_API_KEY"""
    OMDB_API_KEY = os.environ.get('OMDB_API_KEY')
    return jsonify({'OMDB_API_KEY': OMDB_API_KEY})
    
@api.route('/api/TMDB_API_KEY')
def tmdb_api_key():
    """Returns the TMDB_API_KEY"""
    TMDB_API_KEY = os.environ.get('TMDB_API_KEY')
    return jsonify({'TMDB_API_KEY': TMDB_API_KEY})

@api.route('/api/movies')
def json_movies():
    """Returns all movies in the database"""
    movies = MovieSchema(many=True).dump(Movie.query.all())
    return jsonify(movies)

@api.route('/api/series')
def json_series():
    """Returns all shows in the database"""
    series = SeriesSchema(many=True).dump(Series.query.all())
    return jsonify(series)

@api.route('/api/tags')
def json_tags():
    """Returns all tags in the database"""
    tags = TagSchema(many=True).dump(Tag.query.all())
    return jsonify(tags)

@api.route('/api/characters')
def json_characters():
    """Returns all characters in the database"""
    characters = CharacterSchema(many=True).dump(Character.query.all())
    return jsonify(characters)