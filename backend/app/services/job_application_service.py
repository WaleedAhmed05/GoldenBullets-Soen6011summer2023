from models.job_post import JobPost
from models.interview import Invite
from models.job_application import JobApplication
from models.user import User
from models.candidate import Candidate
from services.notification import NotificationService
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
			# Get candidate by user id
			candidate = Candidate.query.get(user.id)
			cv = request.json['cv'] if 'cv' in request.json else None
			cover_letter = request.json['cover_letter'] if 'cover_letter' in request.json else None
			# Create job_application instance
			job_application = JobApplication(cv=cv, cover_letter=cover_letter, job_post_id=id, candidate_id=candidate.id)
			db.session.add(job_application)
			db.session.commit()
			# Create notification for employer
			job_post = JobPost.query.get(id)
			NotificationService.create_notification(job_post.employer_id, 'New job application', f'You have a new job application for {job_post.title}')
			return job_application.serialize()
		except Exception as e:
			print('error', e)
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
			# For each application, get candidate and attach to application
			app_with_candidate = []
			for application in applications:
				candidate = Candidate.query.get(application.candidate_id)
				application_dict = application.serialize()
				application_dict['candidate'] = candidate.serialize()
				app_with_candidate.append(application_dict)
			return app_with_candidate if app_with_candidate else []
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

			return application.serialize() if application else {'error': 'Job application not found'}
		except Exception as e:
			return {'error': str(e)}, 400
		
	@staticmethod
	@jwt_required()
	def update_job_post_application(application_id, status):
		try:
			# Check if user is the owner of the job post
			user_email = get_jwt_identity()
			user = User.query.filter_by(email=user_email).first()
			job_application = JobApplication.query.get(application_id)
			job = JobPost.query.get(job_application.job_post_id)
			if user_email is None or user.id != job.employer_id:
				return {'error': 'Unauthorized'}, 401
			
			# Update job application status
			job_application.status = status
			db.session.commit()

			# Create notification for candidate
			if status == 'interview':
				NotificationService.create_notification(job_application.candidate_id, 'Interview invitation', f'You have been invited for an interview for {job.title} at {job_application.job_post.company.name}')
			else:
				NotificationService.create_notification(job_application.candidate_id, 'Job application status', f'Your job application for {job.title} at {job_application.job_post.company.name} has been {status}')

			return {'success': True}
		except Exception as e:
			print('error', e)
			return {'error': str(e)}, 400

	@staticmethod
	@jwt_required()
	def set_job_application_interview(application_id, status,invite):
		try:
			# Check if user is the owner of the job post
			user_email = get_jwt_identity()
			user = User.query.filter_by(email=user_email).first()
			job_application = JobApplication.query.get(application_id)
			job = JobPost.query.get(job_application.job_post_id)
			if user_email is None or user.id != job.employer_id:
				return {'error': 'Unauthorized'}, 401

			# Update job application status
			job_application.status = status
			db.session.commit()

			# Create notification for candidate
			NotificationService.create_notification(job_application.candidate_id, 'Interview invitation',
														f'You have been invited for an interview for {job.title} at {job_application.job_post.company.name}\n'
														f'please make sure to be in {invite["location"]} at {invite["date"]} at {invite["time"]}')

			return {'success': True}
		except Exception as e:
			print('error', e)
			return {'error': str(e)}, 400
		
	@staticmethod
	@jwt_required()
	def get_applications_by_candidate():
		try:
			# Get candidate
			user_email = get_jwt_identity()
			user = User.query.filter_by(email=user_email).first()
			candidate = Candidate.query.get(user.id)
			if user_email is None or candidate.id is None:
				return {'error': 'Unauthorized'}, 401
			
			applications = JobApplication.query.filter_by(candidate_id=candidate.id).all()
			# For each application, get job post and attach to application
			app_with_job_post = []
			for application in applications:
				job_post = JobPost.query.get(application.job_post_id)
				application_dict = application.serialize()
				application_dict['job_post'] = job_post.serialize()
				app_with_job_post.append(application_dict)
			return app_with_job_post if app_with_job_post else []
		except Exception as e:
			print('error', e)
			return {'error': str(e)}, 400

	@staticmethod
	@jwt_required()
	def get_job_application_interview(id):
		try:
			# Verify jwt token
			if not get_jwt_identity():
				return {'error': 'Unauthorized'}, 401

			# Check if user is the owner of the job post
			user_email = get_jwt_identity()
			user = User.query.filter_by(email=user_email).first()
			interviews = Invite.query.get(id)
			# For each application, get candidate and attach to application
			app_with_candidate = []
			for interview in interviews:
				application_dict = interview.serialize()
				app_with_candidate.append(application_dict)
			return app_with_candidate if app_with_candidate else []
		except Exception as e:
			return {'error': str(e)}, 400
