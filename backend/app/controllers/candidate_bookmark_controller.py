from services.candidate_bookmark_service import CandidateBookmarkService
from flask import jsonify

# Handling candidate bookmarking operations
class CandidateBookmarkController:
    def bookmark_candidate(candidate_id):
        try:
            return jsonify(CandidateBookmarkService.bookmark_candidate(candidate_id))
        except Exception as e:
            print('Error', e)
            return {'error': str(e)}, 500
        
    def get_bookmarked_candidates():
        try:
            return jsonify(CandidateBookmarkService.get_bookmarked_candidates())
        except Exception as e:
            print('Error', e)
            return {'error': str(e)}, 500
