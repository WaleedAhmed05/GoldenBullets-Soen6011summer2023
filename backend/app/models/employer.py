"""
Model: Employer
"""

from extensions import db
from sqlalchemy import Column, String, func, ForeignKey
from sqlalchemy.types import Integer, DateTime, Text
from .user import User

class Employer(User):
	__tablename__ = 'employer'
	
	id = Column(Integer, ForeignKey('user.id'), primary_key=True)
	company_id = Column(Integer, nullable=False)

	__mapper_args__ = {
		'polymorphic_identity': 'employer',
	}

	def serialize(self):
		return {
			'id': self.id,
			'email': self.email,
			'password': self.password,
			'company_id': self.company.serialize() if self.company else None,
		}
	