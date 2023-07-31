from services.candidate import CandidateService
from flask import jsonify, request

class CandidateController:
    def update_profile(id, request):
        try:
            return CandidateService.update_profile(id, request)
        except Exception as e:
            print('Error: ', e)
            return {'error': str(e)}, 500

    def get_profile(id):
        try:
            profile = jsonify(CandidateService.get_profile(id))
            return profile
        except Exception as e:
            print('Error: ', e)
            return {'error': str(e)}, 500
