"""
Model: Notification
"""

from extensions import db
from sqlalchemy import Column, String, func, ForeignKey
from sqlalchemy.types import Integer, DateTime, Text

class Notification(db.Model):
	__tablename__ = 'notification'
	
	id = Column(Integer, primary_key=True, autoincrement=True)
	user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
	title = Column(String(255), nullable=False)
	body = Column(Text, nullable=True)
	created_at = Column(DateTime, nullable=False, server_default=func.now())
	
	def serialize(self):
		return {
			'id': self.id,
			'user_id': self.user_id,
			'title': self.title,
			'body': self.body,
			'created_at': self.created_at,
		}