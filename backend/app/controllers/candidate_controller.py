from services.candidate import CandidateService
from flask import jsonify

class candidate_controller:
    def update_profile():
        try:
            return CandidateService.update_profile()
        except Exception as e:
            return {'error': str(e)}, 500


    def get_profile(id):
        try:
            profile = jsonify(CandidateService.get_profile(id))
            return profile
        except Exception as e:
            return {'error': str(e)}, 500