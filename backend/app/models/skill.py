"""
Model: Skill
"""

from extensions import db
from sqlalchemy import Column, String, func
from sqlalchemy.types import Integer, DateTime

class Skill(db.Model):
	__tablename__ = 'skill'
	
	id = Column(Integer, primary_key=True)
	name = Column(String(100), nullable=False)
	candidates = db.relationship('Candidate', secondary='candidate_skill', back_populates='skills')
	created_at = Column(DateTime, nullable=False, default=func.now())
	updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

	def serialize(self):
		return {
			'id': self.id,
			'name': self.name,
		}
	