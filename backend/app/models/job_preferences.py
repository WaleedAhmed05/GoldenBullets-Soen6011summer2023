"""
Model: Job_Preferences
"""

from extensions import db
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.types import Integer, Text, Enum
from .job_post import JobTypeEnum

class JobPreferences(db.Model):
	__tablename__ = 'job_preferences'

	id = Column(Integer, primary_key=True)
	candidate_id = Column(Integer, ForeignKey('candidate.id'), nullable=False)
	title = Column(String(100), nullable=False)
	location = Column(String(100), nullable=True)
	job_type = Column(Enum(JobTypeEnum), nullable=True, default=JobTypeEnum.FULL_TIME)

	def serialize(self):
		return {
			'id': self.id,
			'candidate_id': self.candidate_id,
			'title': self.title,
			'location': self.location,
			'job_type': self.job_type.value
		}