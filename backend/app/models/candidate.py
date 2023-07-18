"""
Model: application
"""

from extensions import db
from sqlalchemy import Column, String, func, ForeignKey
from sqlalchemy.types import Integer, DateTime, Text

class Candidate(db.Model):
    __tablename__ = 'candidate'
    id = Column(Integer, primary_key=True)
    profile = Column(String(1000), nullable=False)
    candidate_id = Column(Integer, nullable=False)
    jobpost_id = Column(Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'candidate_id': self.candidate_id,
            'jobpost_id': self.jobpost_id,
            'profile': self.profile,
        }

    def __init__(self, id, profile,candidate_id, jobpost_id):
        self.id = id
        self.profile = profile
        self.candidate_id = candidate_id
        self.jobpost_id = jobpost_id

    def changeProf(self,profile):  #for later change profile
        self.profile = profile
