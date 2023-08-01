from models.user import User
from models.candidate import Candidate
from extensions import db
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from flask import request

class CandidateService:
	@staticmethod
	@jwt_required()
	def update_profile(id, request):
		try:
			# Verify jwt token
			user_email = get_jwt_identity()
			if not user_email:
				return {'error': 'Unauthorized'}, 401
			# Make sure user is a candidate
			user = User.query.filter_by(email=user_email).first()
			if user.type != 'candidate':
				return {'error': 'Unauthorized'}, 401

			candidate = Candidate.query.filter_by(id=user.id).first()
			# Update each attribute if it exists in request.json
			if 'first_name' in request.json:
				user.first_name = request.json['first_name']
			if 'last_name' in request.json:
				user.last_name = request.json['last_name']
			if 'work_experience' in request.json:
				candidate.work_experience = request.json['work_experience']
			if 'education' in request.json:
				candidate.education = request.json['education']
			if 'certifications' in request.json:
				candidate.certifications = request.json['certifications']
			if 'resume_url' in request.json:
				candidate.resume_url = request.json['resume_url']
			if 'linkedin_url' in request.json:
				candidate.linkedin_url = request.json['linkedin_url']
			if 'github_url' in request.json:
				candidate.github_url = request.json['github_url']

			# Commit changes to database
			db.session.commit()
			return {'message': 'Profile updated successfully'}, 200
		except Exception as e:
			print('Error: ', e)
			return {'error': str(e)}, 500
		
	@staticmethod
	@jwt_required()
	def get_profile(id):
		try:
			# Verify jwt token
			if not get_jwt_identity():
				return {'error': 'Unauthorized'}, 401
			user = User.query.filter_by(id=id).first()
			candidate = Candidate.query.filter_by(id=user.id).first()
			if not candidate:
				return {'error': 'Candidate not found'}, 404			
			return candidate.serialize()
		except Exception as e:
			print('Error: ', e)
			return {'error': str(e)}, 500

