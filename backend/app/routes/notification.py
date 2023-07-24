from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from controllers.notification import NotificationController

notification_routes = Blueprint('notification_routes', __name__, url_prefix='/api/notifications')

@jwt_required()
@notification_routes.route('/<int:user_id>', methods=['GET'])
def get_notifications(user_id):
	try:
		return NotificationController.get_notifications(user_id)
	except Exception as e:
		return jsonify({'error': str(e)}), 500
