from services.notification import NotificationService
from flask import jsonify

class NotificationController:
	def get_notifications():
		try:
			notifications = jsonify(NotificationService.get_notifications())
			return notifications
		except Exception as e:
			return {'error': str(e)}, 500
