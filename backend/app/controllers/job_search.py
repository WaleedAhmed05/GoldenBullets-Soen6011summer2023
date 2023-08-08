from services.job_search import JobSearchService
from flask import jsonify

class JobSearchController:

    def filter_jobs(args):
        try:
            filtered_jobs = jsonify(JobSearchService.filter_jobs(args))
            return filtered_jobs
        except Exception as e:
            print('Error', e)
            return {'error': str(e)}, 500
