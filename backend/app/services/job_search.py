from models.job_post import JobPost
from flask import request


class JobSearchService:
    @staticmethod
    def filter_jobs(args):
        try:
            title = args.get('title')
            location = args.get('location')
            job_type = args.get('job_type')

            # Filter by one param at a time
            if title:
                filtered_jobs = JobPost.query.filter_by(title=title)
            elif location:
                filtered_jobs = JobPost.query.filter_by(location=location)
            elif job_type:
                filtered_jobs = JobPost.query.filter_by(job_type=job_type)
            else:
                filtered_jobs = JobPost.query.all()
            
            return [filtered_job.serialize() for filtered_job in filtered_jobs]
        except Exception as e:
            print('Error', e)
            return {'error': str(e)}, 500
