from models.notification import Notification
from models.user import User
from extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity

class NotificationService:
	@staticmethod
	def create_notification(user_id, title, body):
		try:
			notification = Notification(user_id=user_id, title=title, body=body)
			db.session.add(notification)
			db.session.commit()
			return notification.serialize()
		except Exception as e:
			return {'error': str(e)}, 400
		
	@staticmethod
	@jwt_required()
	def get_notifications():
		try:
			# Verify jwt token
			user_email = get_jwt_identity()
			user = User.query.filter_by(email=user_email).first()
			if not user_email or user is None:
				return {'error': 'Unauthorized'}, 401
			
			notifications = Notification.query.filter_by(user_id=user.id).all()
			return [notification.serialize() for notification in notifications]
		except Exception as e:
			return {'error': str(e)}, 400
