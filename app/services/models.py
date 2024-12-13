from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    company = db.Column(db.String(100))
    email = db.Column(db.String(100))
    role = db.Column(db.String(100))
    notes = db.Column(db.Text)
