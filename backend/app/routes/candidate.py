from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from controllers.CandidateController import CandidateController

candidate_routes = Blueprint('candidate_routes', __name__, url_prefix='/api/candidate')

@jwt_required()
@candidate_routes.route('/', methods=['PUT'])
def update_profile():
	try:
		return CandidateController.update_profile()
	except Exception as e:
		return jsonify({'error': str(e)}), 500
	
@candidate_routes.route('/<int:id>', methods=['GET'])
def get_profile(id):
	try:
		return CandidateController.get_profile(id)
	except Exception as e:
		return jsonify({'error': str(e)}), 500

@candidate_routes.route('/<int:id>/employers', methods=['GET'])
def get_employers(id):
	try:
		return CandidateController.get_employers(id)
	except Exception as e:
		return jsonify({'error': str(e)}), 500
