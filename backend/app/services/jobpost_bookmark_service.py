from models.bookmark import Bookmark
from models.user import User
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import db

class JobpostBookmarkService:
	@staticmethod
	@jwt_required()
	def bookmark_jobpost(job_id):
		try:
			# Get user from jwt token
			user_email = get_jwt_identity()
			user = User.query.filter_by(email=user_email).first()
			# Check if user type is candidate
			if user.type != 'candidate':
				return {'error': 'Unauthorized'}, 401
			
			prev_bookmark = Bookmark.query.filter_by(employer_id = None, candidate_id=user.id, job_id=job_id).first()
			if prev_bookmark is None:
				bookmark = Bookmark(employer_id=None, candidate_id=user.id, job_id=job_id)
				db.session.add(bookmark)
				db.session.commit()
				return bookmark.serialize()
			else:
				# Remove bookmark
				db.session.delete(prev_bookmark)
				db.session.commit()
				return {'message': 'Bookmark removed'}
		except Exception as e:
			print('error', e)
			return {'error': str(e)}, 500
		
	@staticmethod
	@jwt_required()
	def get_bookmarked_jobs():
		try:
			# Get user from jwt token
			user_email = get_jwt_identity()
			user = User.query.filter_by(email=user_email).first()
			# Check if user type is candidate
			if user.type != 'candidate':
				return {'error': 'Unauthorized'}, 401
			
			bookmarks = Bookmark.query.filter_by(employer_id = None, candidate_id=user.id).all()
			return [bookmark.serialize() for bookmark in bookmarks]
		except Exception as e:
			print('error', e)
			return {'error': str(e)}, 500
