"""
Model: CandidateSkill
"""

from extensions import db
from sqlalchemy import Column, String, func, ForeignKey
from sqlalchemy.types import Integer, DateTime

class CandidateSkill(db.Model):
	__tablename__ = 'candidate_skill'

	id = Column(Integer, primary_key=True)
	candidate_id = Column(Integer, ForeignKey('candidate.id'), nullable=False)
	skill_id = Column(Integer, ForeignKey('skill.id'), nullable=False)
	created_at = Column(DateTime, nullable=False, default=func.now())
	updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

	def serialize(self):
		return {
			'id': self.id,
			'candidate_id': self.candidate_id,
			'skill_id': self.skill_id,
		}
	