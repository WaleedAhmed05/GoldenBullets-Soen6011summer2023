from services.filter_jobs_service import FilterJobsService
from flask import jsonify

class FilterJobsController:

    def get_filtered_jobs():
        try:
            filtered_jobs = jsonify(FilterJobsService.get_filtered_jobs())
            return filtered_jobs
        except Exception as e:
            return {'error': str(e)}, 500