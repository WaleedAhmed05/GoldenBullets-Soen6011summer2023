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
