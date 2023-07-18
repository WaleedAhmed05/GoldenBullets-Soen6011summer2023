"""
Model: JobPost
"""

from extensions import db
from sqlalchemy import Column, String, func
from sqlalchemy.types import Integer, DateTime, Text, Enum
import enum
from .employer import Employer
from .company import Company

class JobTypeEnum(enum.Enum):
	FULL_TIME = 'full_time'
	PART_TIME = 'part_time'
	CONTRACT = 'contract'
	INTERNSHIP = 'internship'
	
class JobPost(db.Model):
	__tablename__ = 'job_post'
	
	id = Column(Integer, primary_key=True)
	title = Column(String(100), nullable=False)
	description = Column(Text, nullable=False)
	location = Column(String(100), nullable=False)
	salary = Column(String(100), nullable=False)
	job_type = Column(Enum(JobTypeEnum), nullable=False, default=JobTypeEnum.FULL_TIME)
	employer_id = Column(Integer, db.ForeignKey('employer.id'), nullable=False)
	company_id = Column(Integer, db.ForeignKey('company.id'), nullable=False)
	company = db.relationship('Company', backref=db.backref('job_posts', lazy=True))
	created_at = Column(DateTime, nullable=False, default=func.now())
	updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

	def serialize(self):
		return {
			'id': self.id,
			'title': self.title,
			'description': self.description,
			'location': self.location,
			'salary': self.salary,
			'job_type': self.job_type.value,
			'employer_id': self.employer_id,
			'company_id': self.company_id,
			'company': self.company.serialize() if self.company else None,
			'created_at': self.created_at,
			'updated_at': self.updated_at
		}

