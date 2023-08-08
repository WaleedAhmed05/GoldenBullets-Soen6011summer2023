from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from controllers.invite_candidate_controller import InviteCandidateController

invite_candidate_routes = Blueprint('invite_candidate_routes', __name__, url_prefix='/api/invite_candidate')

# @jwt_required()
@invite_candidate_routes.route('/', methods=['POST'])
def invite_candidate():
	try:
		return InviteCandidateController.invite_candidate(request)
	except Exception as e:
		return jsonify({'error': str(e)}), 500