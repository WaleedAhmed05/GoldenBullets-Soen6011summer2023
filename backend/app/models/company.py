"""
Model: Company
"""

from extensions import db
from sqlalchemy import Column, String, func
from sqlalchemy.types import Integer, DateTime, Text

class Company(db.Model):
	__tablename__ = 'company'
	
	id = Column(Integer, primary_key=True)
	name = Column(String(100), nullable=False)
	description = Column(Text, nullable=False)
	website = Column(String(100), nullable=False)
	industry = Column(String(100), nullable=False)
	num_employees = Column(Integer, nullable=False)	
	created_at = Column(DateTime, nullable=False, default=func.now())
	updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

	def serialize(self):
		return {
			'id': self.id,
			'name': self.name,
			'description': self.description,
			'website': self.website,
			'industry': self.industry,
			'num_employees': self.num_employees,
			'created_at': self.created_at,
			'updated_at': self.updated_at
		}
	