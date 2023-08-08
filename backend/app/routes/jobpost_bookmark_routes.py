from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from controllers.jobpost_bookmark_controller import JobpostBookmarkController

jobpost_bookmark_routes = Blueprint('jobpost_bookmark_routes', __name__, url_prefix='/api/jobs/bookmark')

@jwt_required()
@jobpost_bookmark_routes.route('/<int:id>', methods=['POST'])
def bookmark_jobpost(id):
	try:
		return JobpostBookmarkController.bookmark_jobpost(id)
	except Exception as e:
		return jsonify({'error': str(e)}), 500
	
@jwt_required()
@jobpost_bookmark_routes.route('/', methods=['GET'])
def get_bookmarked_jobs():
	try:
		return JobpostBookmarkController.get_bookmarked_jobs()
	except Exception as e:
		print('Error', e)
		return jsonify({'error': str(e)}), 500