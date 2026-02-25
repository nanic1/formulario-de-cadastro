from . import db

# models for all tables on db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(150), unique=True)
    number = db.Column(db.String(20))
    password = db.Column(db.String(200))
    gender = db.Column(db.String(50))