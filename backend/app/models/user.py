"""
Model: User
"""

from extensions import db
from sqlalchemy import Column, String, func
from sqlalchemy.types import Integer, DateTime, Text, Enum
import enum

class User(db.Model):
	__tablename__ = 'user'
	
	id = Column(Integer, primary_key=True)
	first_name = Column(String(100), nullable=False)
	last_name = Column(String(100), nullable=False)
	email = Column(String(100), nullable=False)
	password = Column(String(100), nullable=False)
	oauth_token = Column(String(255), nullable=False)
	oauth_token_secret = Column(String(255), nullable=False)
	created_at = Column(DateTime, nullable=False, default=func.now())
	updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())
	type = Column(String(50))
	
	__mapper_args__ = {
		'polymorphic_identity': 'user',
		'polymorphic_on': type
	}