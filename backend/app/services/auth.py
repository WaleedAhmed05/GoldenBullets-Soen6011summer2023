from flask import url_for, request
from flask_dance.contrib.google import google
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity
from flask import session
from os import getenv
from extensions import db
from models.user import User
from models.candidate import Candidate
from models.employer import Employer
from models.job_post import JobPost

class AuthService:
	@staticmethod
	def google_login():
		# Get `type` query param
		user_type = request.args.get('type')
		# Save user type in session
		if user_type:
			session['user_type'] = user_type
		# Return google login url
		return url_for('google.login')

	@staticmethod
	def google_login_callback():
		try:
			if not google.authorized:
				return url_for('google.login')

			account_info = google.get('/oauth2/v2/userinfo')
			if account_info.ok:
				account_info_json = account_info.json()
				email = account_info_json['email']
				# Check if user is in database
				user = User.query.filter_by(email=email).first()
				if not user:
					# Create user 
					name = account_info_json['name']
					# Split name into first and last name
					name_split = name.split(' ')
					first_name = name_split[0]
					last_name = name_split[-1]
					# Get user type from session
					user_type = session.get('user_type') or None
					if not user_type:
						return {'error': 'User type not found'}
					
					if user_type == 'candidate':
						user = Candidate(
							email=email,
							first_name=first_name,
							last_name=last_name
						)
					elif user_type == 'employer':
						user = Employer(
							email=email,
							first_name=first_name,
							last_name=last_name
						)
					else:
						return {'error': 'Invalid user type'}
					# Add user to database
					db.session.add(user)
					db.session.commit()
				# Create JWT token
				access_token = create_access_token(identity=email)
				# Return url to frontend with JWT token
				redirect_url = request.args.get('redirect_url') or getenv('FRONTEND_URL')
				return f'{redirect_url}?token={access_token}'
			else:
				return {'error': 'Failed to fetch user info'}
		except Exception as e:
			return {'error': str(e)}
		
	@staticmethod
	def user_data():
		try:
			user_email = get_jwt_identity()
			user = User.query.filter_by(email=user_email).first()
			if user:
				# Get company_id from employer model if user is employer
				if user.type == 'employer':
					employer = Employer.query.filter_by(id=user.id).first()
					data = employer.serialize()
					data['id'] = user.id
					data['type'] = user.type
					# Add job posts to data
					job_posts = JobPost.query.filter_by(employer_id=user.id).all()
					data['job_posts'] = [job_post.serialize() for job_post in job_posts]
					return data
				elif user.type == 'candidate':
					candidate = Candidate.query.filter_by(id=user.id).first()
					data = candidate.serialize()
					data['id'] = user.id
					data['type'] = user.type
					return data
			else:
				return {'error': 'User not found'}
		except Exception as e:
			print('Error', e)
			return {'error': str(e)}

		