from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from controllers.candidate_jobpreferences_controller import CandidateJobPreferencesController

candidate_jobpreferences_routes = Blueprint('candidate_jobpreferences_routes', __name__, url_prefix='/api/setjobpreference')

# @jwt_required()
@candidate_jobpreferences_routes.route('/', methods=['POST'])
def set_job_preference():
	try:
		return CandidateJobPreferencesController.set_job_preference(request)
	except Exception as e:
		return jsonify({'error': str(e)}), 500