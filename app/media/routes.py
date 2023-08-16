"""Summary this page contains the routes for the movies blueprint."""

from flask import render_template, request, jsonify
from app.media import media
# from app.media.models.comment_model import Comment
# # from app.media.forms.comment_form import CommentForm
# from app.media.models.review_model import Review
# from app.media.forms.review_form import ReviewForm
from app import db
from app.models.star_trek_models import Series, Movie, Staff, Season, Episode, Company, Performer
from app.helpers import MemoryAlphaScraper, replace_space

@media.route('/')
def media_index():
    """This page shows all media related to the Star Trek Universe."""
    return render_template('media.html')


@media.route('/movies')
def movies():
    """This page shows all the movies in the database."""
    movies = Movie.query.all()
    print(Movie.query.first())
    return render_template('movies.html', movies=movies, title="Movies")

@media.route('/movie/<title>')
def movie(title):
    """Return a single movie."""
    movie = Movie.query.filter_by(title=title).first()
    review_form = ReviewForm()
    return render_template('movie.html', movie=movie, title=title, form=review_form)
    
@media.route('/shows')
def shows():
    """Shows an index of shows in the database."""
    shows = Series.query.all()
    return render_template('shows.html', shows=shows, title="Shows")

@media.route('/show/<title>')
def show(title):
    """Return a single show."""
    show = Series.query.filter_by(title=title).first()
    return render_template('show.html', show=show, title=title)

@media.route('/performers')
def performers():
    """Returns all the performers from the database which is also the cast of characters."""
    performers = Performer.query.order_by(Performer.name).all()
    page = request.args.get('page', 1, type=int)
    paginated_performers = Performer.query.order_by(Performer.name).paginate(page=page, per_page=25)
    return render_template('performers.html', performers=performers, title="Performers", paginated_performers=paginated_performers, page=page)


@media.route('/performer/<name>')
def performer(name):
    """Returns a single performer."""
    performer = Performer.query.filter_by(name=name).first()
    if performer:
        try:
            scrapped_performer = MemoryAlphaScraper(replace_space(name))
            summary = scrapped_performer.get_summary()
            if summary:
                return render_template('performer.html', performer=performer, title=name, summary=summary)
            else:
                print("No summary found.")
                raise TypeError
        except TypeError as e:
            return "Error: " + str(e)
                
    