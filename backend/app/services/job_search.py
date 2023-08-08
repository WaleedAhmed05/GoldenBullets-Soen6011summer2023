from models.job_post import JobPost
from models.company import Company
from flask import request


class JobSearchService:
    @staticmethod
    def filter_jobs(args):
        try:
            title = args.get('title')
            location = args.get('location')
            job_type = args.get('job_type')
            industry = args.get('industry')

            # Filter by one param at a time
            if title:
                filtered_jobs = JobPost.query.filter_by(title=title)
            elif location:
                filtered_jobs = JobPost.query.filter_by(location=location)
            elif job_type:
                filtered_jobs = JobPost.query.filter_by(job_type=job_type)
            elif industry:
                filtered_jobs = JobPost.query.filter(JobPost.company.has(industry=industry))
            else:
                filtered_jobs = []
            
            return [filtered_job.serialize() for filtered_job in filtered_jobs]
        except Exception as e:
            print('Error', e)
            return {'error': str(e)}, 500

    @staticmethod
    def search(args):
        try:
            # Trim whitespace from search query and convert to lowercase
            search_query = args.get('q').strip().lower()
            # Search by title, location, job_type, description, or company name or company industry
            search_results = JobPost.query.filter(JobPost.title.ilike(f'%{search_query}%') | JobPost.location.ilike(f'%{search_query}%') | JobPost.job_type.ilike(f'%{search_query}%') | JobPost.description.ilike(f'%{search_query}%') | JobPost.company.has(name=search_query) | JobPost.company.has(industry=search_query)).all()
            return [search_result.serialize() for search_result in search_results]
        except Exception as e:
            print('Error', e)
            return {'error': str(e)}, 500
    
    @staticmethod
    def list_all_industries():
        try:
            industries = Company.query.with_entities(Company.industry).distinct().all()
            return [industry[0] for industry in industries]
        except Exception as e:
            print('Error', e)
            return {'error': str(e)}, 500
