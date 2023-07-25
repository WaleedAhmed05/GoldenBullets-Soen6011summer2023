from services.invite_candidate_service import InviteCandidateService
from flask import jsonify

class InviteCandidateController:
    def invite_candidate(request):
        try:
            return jsonify(InviteCandidateService.invite_candidate(request))
        except Exception as e:
            return {'error': str(e)}, 500