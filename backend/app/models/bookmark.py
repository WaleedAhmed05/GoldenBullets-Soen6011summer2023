"""
Model: Bookmark
"""

from extensions import db
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, Text

class Bookmark(db.Model):
	__tablename__ = 'bookmark'

	id = Column(Integer, primary_key=True)
	employer_id = Column(Integer, db.ForeignKey('employer.id'), nullable=True)
	candidate_id = Column(Integer, ForeignKey('candidate.id'), nullable=False)
	job_id = Column(Integer, ForeignKey('job_post.id'), nullable=False)

	def serialize(self):
		return {
			'id': self.id,
			'employer_id': self.employer_id,
			'candidate_id': self.candidate_id,
			'job_id': self.job_id
		}