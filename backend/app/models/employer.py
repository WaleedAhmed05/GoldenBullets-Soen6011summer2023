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
	company_id = Column(Integer, ForeignKey('company.id'), nullable=True)

	__mapper_args__ = {
		'polymorphic_identity': 'employer',
	}

	def serialize(self):
		return {
			'id': self.id,
			'first_name': self.first_name,
			'last_name': self.last_name,
			'email': self.email,
			'company_id': self.company_id,
		}
	