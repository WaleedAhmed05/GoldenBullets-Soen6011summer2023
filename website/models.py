from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    role = db.Column(db.String(20))
    notes = db.relationship('Note')
    job_postings = db.relationship('JobPosting')  # New relationship

class JobPosting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    job_type = db.Column(db.String(50))
    address = db.Column(db.String(200))
    salary = db.Column(db.Float)
    # shift_schedule = db.Column(db.String(100))
    # language = db.Column(db.String(50))
    description = db.Column(db.Text)
    requirements = db.Column(db.Text)
    employer_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Relationship with User model