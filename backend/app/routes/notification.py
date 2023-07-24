from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from controllers.notification import NotificationController

notification_routes = Blueprint('notification_routes', __name__, url_prefix='/api/notifications')

@jwt_required()
@notification_routes.route('/', methods=['GET'])
def get_notifications():
	try:
		return NotificationController.get_notifications()
	except Exception as e:
		return jsonify({'error': str(e)}), 500
	
@jwt_required()
@notification_routes.route('/<notification_id>', methods=['PUT'])
def set_notification_as_read(notification_id):
	try:
		return NotificationController.set_notification_as_read(notification_id)
	except Exception as e:
		return jsonify({'error': str(e)}), 500
