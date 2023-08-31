from flask import current_app
from sqlalchemy import or_, and_
from sqlalchemy.orm import aliased
from app.models.star_trek_models import Character

class Search:
    def __init__(self, query):
        self.query = query

    def search(self):
        query = self.query
        if query == '':
            return Character.query.order_by(Character.name).all()
        else:
            return Character.query.filter(Character.name.contains(query)).order_by(Character.name).all()