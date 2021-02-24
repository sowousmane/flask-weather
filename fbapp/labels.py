from flask_sqlalchemy import SQLAlchemy

from .views import app

# Create database connection object
db = SQLAlchemy(app)

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shape = db.Column(db.String(200), nullable=False)
    label = db.Column(db.String(200), nullable=False)

    def __init__(self, description, gender):
        self.description = description
        self.gender = gender

db.create_all()