from models.job_post import JobPost
from models.job_application import JobApplication
from models.user import User
from extensions import db
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity

class JobPostService:
	@staticmethod
	def get_job_posts():
		job_posts = JobPost.query.all()
		return [job_post.serialize() for job_post in job_posts]
	
	@staticmethod
	@jwt_required()
	def get_employer_job_posts():
		try:
			# Verify jwt token
			if not get_jwt_identity():
				return {'error': 'Unauthorized'}, 401
			# Get user email from jwt token
			user_email = get_jwt_identity()
			user = User.query.filter_by(email=user_email).first()
			# Check if user type is employer
			if user.type != 'employer':
				return {'error': 'Unauthorized'}, 401
			
			job_posts = JobPost.query.filter_by(employer_id=user.id).all()
			return [job_post.serialize() for job_post in job_posts]
		except Exception as e:
			return {'error': str(e)}, 500
	
	@staticmethod
	def get_job_post(id):
		return JobPost.query.get(id).serialize()
	
	@staticmethod
	@jwt_required()
	def create_job_post(request):
		try:
			# Verify jwt token
			if not get_jwt_identity():
				return {'error': 'Unauthorized'}, 401
			# Get user email from jwt token
			user_email = get_jwt_identity()
			user = User.query.filter_by(email=user_email).first()
			# Check if user type is employer
			if user.type != 'employer':
				return {'error': 'Unauthorized'}, 401
			
			title = request.json['title']
			description = request.json['description']
			location = request.json['location']
			salary = request.json['salary']
			job_type = request.json['job_type']
			employer_id = user.id
			company_id = request.json['company_id']
			job_post = JobPost(title=title, description=description, location=location, salary=salary, job_type=job_type, employer_id=employer_id, company_id=company_id)
			db.session.add(job_post)
			db.session.commit()

			return job_post.serialize()
		except Exception as e:
			return {'error': str(e)}, 400
	
	@staticmethod
	@jwt_required()
	def update_job_post(id, request):
		try:
			# Verify jwt token
			if not get_jwt_identity():
				return {'error': 'Unauthorized'}, 401
			
			job_post = JobPost.query.get(id)
			# Check if user is the owner of the job post
			user_email = get_jwt_identity()
			user = User.query.filter_by(email=user_email).first()
			if user.id != job_post.employer_id:
				return {'error': 'Unauthorized'}, 401
			
			job_post.title = request.json['title']
			job_post.description = request.json['description']
			job_post.location = request.json['location']
			job_post.salary = request.json['salary']
			job_post.job_type = request.json['job_type']

			db.session.commit()
			return job_post.serialize()
		except Exception as e:
			return {'error': str(e)}, 400
