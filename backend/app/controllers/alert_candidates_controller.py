from services.alert_candidates_service import AlertCandidatesService
from flask import jsonify, request

class AlertCandidatesController:
    def alert_candidates(id):
        try:
            return jsonify(AlertCandidatesService.alert_candidates(id))
        except Exception as e:
            return {'error': str(e)}, 500