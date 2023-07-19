"""
Model: Apply
"""

from extensions import db
from sqlalchemy import Column, String, func
from sqlalchemy.types import Integer, LargeBinary
import enum
from .employer import Employer
from .company import Company


# creating form for applying to a job

class Apply_form(db.Model):
    __tablename__ = 'apply_form'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    # CV pdf file
    cv = Column(LargeBinary, nullable=False)
    # cover letter pdf file
    cover_letter = Column(LargeBinary, nullable=False)
    # job post id
    job_post_id = Column(Integer, db.ForeignKey('job_post.id'), nullable=False)
    # job post
    job_post = db.relationship('JobPost', backref=db.backref('apply_form', lazy=True))
    email = Column(String(100), nullable=False)
    phone = Column(String(100), nullable=False)
    stat = Column(String(100), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'cv': self.cv,
            'cover_letter': self.cover_letter,
            'job_post_id': self.job_post_id,
            'job_post': self.job_post.serialize() if self.job_post else None,
            'email': self.email,
            'phone': self.phone,
            'stat': self.stat
        }
