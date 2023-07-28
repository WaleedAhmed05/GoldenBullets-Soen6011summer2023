from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from controllers.candidate_bookmark_controller import CandidateBookmarkController

candidate_bookmark_routes = Blueprint('candidate_bookmark_routes', __name__, url_prefix='/api/bookmark_candidate')

# @jwt_required()
@candidate_bookmark_routes.route('/', methods=['POST'])
def bookmark_candidate():
	try:
		return CandidateBookmarkController.bookmark_candidate(request)
	except Exception as e:
		return jsonify({'error': str(e)}), 500