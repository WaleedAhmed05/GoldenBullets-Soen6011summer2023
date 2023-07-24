from models.job_post import JobPost
from models.job_application import JobApplication
from models.user import User
from extensions import db
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity

class JobApplicationService:
	@staticmethod
	@jwt_required()
	def apply_job_post(id, request):
		try:
			# Verify jwt token
			if not get_jwt_identity():
				return {'error': 'Unauthorized'}, 401
			
			user_email = get_jwt_identity()
			user = User.query.filter_by(email=user_email).first()
			if user.type != 'candidate':
				return {'error': 'Unauthorized'}, 401
			cv = request.json['cv']
			cover_letter = request.json['cover_letter'] if 'cover_letter' in request.json else None
			# Create job_application instance
			job_application = JobApplication(cv=cv, cover_letter=cover_letter, job_post_id=id, user_id=user.id)
			db.session.add(job_application)
			db.session.commit()
			return job_application.serialize()
		except Exception as e:
			return {'error': str(e)}, 400
		
	@staticmethod
	@jwt_required()
	def get_job_post_applications(id):
		try:
			# Verify jwt token
			if not get_jwt_identity():
				return {'error': 'Unauthorized'}, 401
			
			# Check if user is the owner of the job post
			user_email = get_jwt_identity()
			user = User.query.filter_by(email=user_email).first()
			job_post = JobPost.query.get(id)
			if user.id != job_post.employer_id:
				return {'error': 'Unauthorized'}, 401
			
			applications = JobApplication.query.filter_by(job_post_id=id).all()
			return [application.serialize() for application in applications]
		except Exception as e:
			return {'error': str(e)}, 400
		
	@staticmethod
	@jwt_required()
	def get_job_post_application(job_id, application_id):
		try:
			# Verify jwt token
			if not get_jwt_identity():
				return {'error': 'Unauthorized'}, 401
			
			# Check if user is the owner of the job post
			user_email = get_jwt_identity()
			user = User.query.filter_by(email=user_email).first()
			job_post = JobPost.query.get(job_id)
			if user.id != job_post.employer_id:
				return {'error': 'Unauthorized'}, 401
			
			application = JobApplication.query.get(application_id)
			return application.serialize()
		except Exception as e:
			return {'error': str(e)}, 400