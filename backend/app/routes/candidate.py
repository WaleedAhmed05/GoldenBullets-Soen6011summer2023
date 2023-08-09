from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from controllers.candidate import CandidateController

candidate_routes = Blueprint('candidate_routes', __name__, url_prefix='/api/candidate')

@jwt_required()
@candidate_routes.route('/<int:id>', methods=['PUT'])
def update_profile(id):
	try:
		return CandidateController.update_profile(id, request)
	except Exception as e:
		print('Error: ', e)
		return jsonify({'error': str(e)}), 500
	
@candidate_routes.route('/<int:id>', methods=['GET'])
def get_profile(id):
	try:
		return CandidateController.get_profile(id)
	except Exception as e:
		print('Error: ', e)
		return jsonify({'error': str(e)}), 500

@candidate_routes.route('/', methods=['GET'])
def get_candidates():
	try:
		return CandidateController.get_candidates()
	except Exception as e:
		print('Error: ', e)
		return jsonify({'error': str(e)}), 500
