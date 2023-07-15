from models.job_post import JobPost

class JobPostService:
    @staticmethod
    def get_job_posts():
        return JobPost.query.all()
    
    @staticmethod
    def get_job_post(id):
        return JobPost.query.get(id).serialize()