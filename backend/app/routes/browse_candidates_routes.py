from flask import Blueprint, request, jsonify
from controllers.browse_candidates_controller import BrowseCandidatesController

browse_candidates_routes = Blueprint('browse_candidates_routes', __name__, url_prefix='/api/browse_candidates')

@browse_candidates_routes.route('/allcandidates', methods=['GET'])
def get_all_candidates():
	try:
		return BrowseCandidatesController.get_all_candidates()
	except Exception as e:
		return jsonify({'error': str(e)}), 500

@browse_candidates_routes.route('/allcandidateskills', methods=['GET'])
def get_all_skills():
	try:
		return BrowseCandidatesController.get_all_candidateskills()
	except Exception as e:
		return jsonify({'error': str(e)}), 500