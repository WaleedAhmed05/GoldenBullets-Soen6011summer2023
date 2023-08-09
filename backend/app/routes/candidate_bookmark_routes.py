from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from controllers.candidate_bookmark_controller import CandidateBookmarkController

candidate_bookmark_routes = Blueprint('candidate_bookmark_routes', __name__, url_prefix='/api/bookmark_candidate')

@jwt_required()
@candidate_bookmark_routes.route('/<int:candidate_id>', methods=['POST'])
def bookmark_candidate(candidate_id):
	try:
		return CandidateBookmarkController.bookmark_candidate(candidate_id)
	except Exception as e:
		print('Error', e)
		return jsonify({'error': str(e)}), 500
	
@jwt_required()
@candidate_bookmark_routes.route('/', methods=['GET'])
def get_bookmarked_candidates():
	try:
		return CandidateBookmarkController.get_bookmarked_candidates()
	except Exception as e:
		print('Error', e)
		return jsonify({'error': str(e)}), 500