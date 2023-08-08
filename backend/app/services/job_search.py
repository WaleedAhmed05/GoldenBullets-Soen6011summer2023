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
        
    @staticmethod
    def search(args):
        try:
            # Trim whitespace from search query and convert to lowercase
            search_query = request.args.get('q').strip().lower()
            # Search by title, location, job_type, description, or company name. Company is a relationship
            search_results = JobPost.query.filter(JobPost.title.ilike(f'%{search_query}%') | JobPost.location.ilike(f'%{search_query}%') | JobPost.job_type.ilike(f'%{search_query}%') | JobPost.description.ilike(f'%{search_query}%') | JobPost.company.has(name=search_query)).all()
            return [search_result.serialize() for search_result in search_results]
        except Exception as e:
            print('Error', e)
            return {'error': str(e)}, 500
        