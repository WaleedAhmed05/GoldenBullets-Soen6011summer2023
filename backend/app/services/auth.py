from flask import url_for, request
from flask_dance.contrib.google import google
from flask_jwt_extended import JWTManager, create_access_token
from os import getenv
from extensions import db
from models.user import User

class AuthService:
	@staticmethod
	def google_login():
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
				user = User(email=email, 
				first_name=first_name, last_name=last_name)
				db.session.add(user)
				db.session.commit()
			# Create JWT token
			access_token = create_access_token(identity=email)
			# Return url to frontend with JWT token
			redirect_url = request.args.get('redirect_url') or getenv('FRONTEND_URL')
			return f'{redirect_url}/login?token={access_token}'
		else:
			return {'error': 'Failed to fetch user info'}

		