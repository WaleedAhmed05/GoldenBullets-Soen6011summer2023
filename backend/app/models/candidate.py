"""
Model: Candidate
"""

from extensions import db
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, Text
from sqlalchemy.dialects.mysql import JSON
from .user import User

class Candidate(User):
	__tablename__ = 'candidate'
	
	id = Column(Integer, ForeignKey('user.id'), primary_key=True)
	user = db.relationship('User', backref='candidate', lazy=True)
	work_experience = Column(JSON)
	education = Column(JSON)
	certifications = Column(JSON)
	resume_url = Column(Text)
	linkedin_url = Column(Text)
	github_url = Column(Text)

	__mapper_args__ = {
		'polymorphic_identity': 'candidate',
	}

	def serialize(self):
		return {
			'id': self.id,
			'email': self.email,
			'first_name': self.first_name,
			'last_name': self.last_name,
			'work_experience': self.work_experience,
			'education': self.education,
			'certifications': self.certifications,
			'resume_url': self.resume_url,
			'linkedin_url': self.linkedin_url,
			'github_url': self.github_url,
		}
	