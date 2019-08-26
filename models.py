"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Cupcake(db.Model):

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text)
    size = db.Column(db.Text)
    rating = db.Column(db.Float)
    image = db.Column(db.Text)


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
