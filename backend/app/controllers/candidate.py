from services.candidate import CandidateService
from flask import jsonify, request

class CandidateController:
    # Method to update a candidate's profile
    def update_profile(id, request):
        try:
            return CandidateService.update_profile(id, request)
        except Exception as e:
            print('Error: ', e)
            return {'error': str(e)}, 500

    # Method to retrieve a candidate's profile based on the provided 'id'
    def get_profile(id):
        try:
            profile = jsonify(CandidateService.get_profile(id))
            return profile
        except Exception as e:
            print('Error: ', e)
            return {'error': str(e)}, 500
        
    # Method to retrieve all candidates
    def get_candidates():
        try:
            return CandidateService.get_candidates()
        except Exception as e:
            print('Error: ', e)
            return {'error': str(e)}, 500
