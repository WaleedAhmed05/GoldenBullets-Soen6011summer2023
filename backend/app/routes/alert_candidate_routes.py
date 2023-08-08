from flask import Blueprint, request, jsonify
from controllers.alert_candidates_controller import AlertCandidatesController

alert_candidates_routes = Blueprint('alert_candidates_routes', __name__, url_prefix='/api/alert_candidates')


@alert_candidates_routes.route('/<int:id>', methods=['GET'])
def alert_candidates(id):
	try:
		return AlertCandidatesController.alert_candidates(id)
	except Exception as e:
		return jsonify({'error': str(e)}), 500