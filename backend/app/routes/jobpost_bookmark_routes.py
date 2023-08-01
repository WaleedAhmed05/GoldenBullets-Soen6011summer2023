from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from controllers.jobpost_bookmark_controller import JobpostBookmarkController

jobpost_bookmark_routes = Blueprint('jobpost_bookmark_routes', __name__, url_prefix='/api/bookmark_jobpost')

# @jwt_required()
@jobpost_bookmark_routes.route('/', methods=['POST'])
def bookmark_jobpost():
	try:
		return JobpostBookmarkController.bookmark_jobpost(request)
	except Exception as e:
		return jsonify({'error': str(e)}), 500