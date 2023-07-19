from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from controllers.candidate_controller import candidate_controller

candidate_routes = Blueprint('candidate_routes', __name__, url_prefix='/api/candidate')

@jwt_required()
@candidate_routes.route('/', methods=['PUT'])
def update_profile():
	try:
		return candidate_controller.update_profile()
	except Exception as e:
		return jsonify({'error': str(e)}), 500
	
# @jwt_required()
@candidate_routes.route('/<int:id>', methods=['GET'])
def get_profile(id):
	try:
		return candidate_controller.get_profile(id)
	except Exception as e:
		return jsonify({'error': str(e)}), 500