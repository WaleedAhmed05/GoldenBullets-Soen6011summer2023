"""
Model: Interview
"""

from extensions import db
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, DateTime, Text


class Invite(db.Model):
    __tablename__ = 'interview'

    id = Column(Integer, primary_key=True)
    application_id = Column(Integer, ForeignKey('job_application.id'), nullable=False)
    interview_date = Column(DateTime, nullable=False)
    interview_time = Column(DateTime, nullable=False)
    interview_location = Column(Text, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'application_id': self.application_id,
            'interview_date': self.interview_date,
            'interview_time': self.interview_time,
            'interview_location': self.interview_location,
        }


# /// id and message