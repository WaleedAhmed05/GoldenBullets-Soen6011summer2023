from services.candidates_browse_service import BrowseCandidatesService
from flask import jsonify

class BrowseCandidatesController:

    def get_all_candidates():
        try:
            all_candidate_profiles = jsonify(BrowseCandidatesService.get_all_candidates())
            return all_candidate_profiles
        except Exception as e:
            return {'error': str(e)}, 500

    def get_all_candidateskills():
        try:
            all_candidateskills = jsonify(BrowseCandidatesService.get_all_candidateskills())
            return all_candidateskills
        except Exception as e:
            return {'error': str(e)}, 500
