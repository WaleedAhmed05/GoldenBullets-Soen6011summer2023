from services.jobpost_bookmark_service import JobpostBookmarkService
from flask import jsonify

class JobpostBookmarkController:
    def bookmark_jobpost(id):
        try:
            return jsonify(JobpostBookmarkService.bookmark_jobpost(id)), 200
        except Exception as e:
            return {'error': str(e)}, 500
        
    def get_bookmarked_jobs():
        try:
            return jsonify(JobpostBookmarkService.get_bookmarked_jobs()), 200
        except Exception as e:
            return {'error': str(e)}, 500