from services.candidate_bookmark_service import CandidateBookmarkService
from flask import jsonify

class CandidateBookmarkController:
    def bookmark_candidate(request):
        try:
            return jsonify(CandidateBookmarkService.bookmark_candidate(request))
        except Exception as e:
            return {'error': str(e)}, 500