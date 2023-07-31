from services.candidate import CandidateService
from flask import jsonify

class CandidateController:
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

    def get_employers(id):
        try:
            employers = jsonify(CandidateService.get_potential_employer(id))
            return employers
        except Exception as e:
            return {'error': str(e)}, 500