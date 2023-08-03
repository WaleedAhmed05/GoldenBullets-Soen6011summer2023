"""
Model: JobApplication
"""

from extensions import db
from sqlalchemy import Column, String, func
from sqlalchemy.types import Integer, Enum, DateTime
import enum

# Defining an enumeration for application status
class ApplicationStatusEnum(enum.Enum):
    PENDING = 'pending'
    APPROVED = 'approved'
    REJECTED = 'rejected'
    INTERVIEW = 'interview'

class JobApplication(db.Model):
    __tablename__ = 'job_application'

    id = Column(Integer, primary_key=True)
    candidate_id = Column(Integer, db.ForeignKey('candidate.id'), nullable=False)
    job_post_id = Column(Integer, db.ForeignKey('job_post.id'), nullable=False)
    status = Column(Enum(ApplicationStatusEnum), nullable=False, default=ApplicationStatusEnum.PENDING)
    cv = Column(String(255), nullable=True)
    cover_letter = Column(String(255), nullable=True)
    job_post = db.relationship('JobPost', backref=db.backref('job_applications', lazy=True))
    created_at = Column(DateTime, nullable=False, server_default=func.now())

    def serialize(self):
        return {
            'id': self.id,
            'candidate_id': self.candidate_id,
            'job_post_id': self.job_post_id,
            'status': self.status.value if self.status else None,
            'cv': self.cv,
            'cover_letter': self.cover_letter,
            'job_post': self.job_post.serialize() if self.job_post else None,
            'created_at': self.created_at,
        }
