from models.job_post import JobPost
from flask import request


class FilterJobsService:

    @staticmethod
    def get_filtered_jobs():

        try:
            ftitle = request.args.get('title')
            flocation = request.args.get('location')
            fjob_type = request.args.get('job_type')

            filtered_jobs = JobPost.query.filter_by(title=ftitle, location=flocation,
                                           job_type=fjob_type)

            return [filtered_job.serialize() for filtered_job in filtered_jobs]
        except Exception as e:
            return {'error': str(e)}, 500