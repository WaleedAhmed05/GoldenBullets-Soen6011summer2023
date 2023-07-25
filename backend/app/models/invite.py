"""
Model: Invite
"""

from extensions import db
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, Text


class Invite(db.Model):
	__tablename__ = 'invite'

	id = Column(Integer, primary_key=True)
	job_id = Column(Integer, ForeignKey('job_post.id'), nullable=False)
	candidate_id = Column(Integer, ForeignKey('candidate.id'), nullable=False)

	def serialize(self):
		return {
			'id': self.id,
			'job_id':self.job_id,
			'candidate_id': self.candidate_id,
		}