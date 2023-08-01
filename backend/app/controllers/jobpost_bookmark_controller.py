from services.jobpost_bookmark_service import JobpostBookmarkService
from flask import jsonify

class JobpostBookmarkController:
    def bookmark_jobpost(request):
        try:
            return jsonify(JobpostBookmarkService.bookmark_jobpost(request))
        except Exception as e:
            return {'error': str(e)}, 500