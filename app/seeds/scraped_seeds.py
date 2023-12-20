from app.models.star_trek_models import Series

# This is a seed file for base line routes and pre populated popular data for the website

# Need to get popular characters for all the series
series = Series.get_series_titles()
print([title for title in series])


