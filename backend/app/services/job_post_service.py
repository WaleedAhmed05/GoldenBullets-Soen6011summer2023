from models.job_post import JobPost

class JobPostService:
    @staticmethod
    def get_job_posts():
        job_posts = JobPost.query.all()
        return [job_post.serialize() for job_post in job_posts]
    
    @staticmethod
    def get_job_post(id):
        return JobPost.query.get(id).serialize()