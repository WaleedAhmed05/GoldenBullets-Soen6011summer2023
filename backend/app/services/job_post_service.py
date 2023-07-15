from models.job_post import JobPost

class JobPostService:
    @staticmethod
    def get_job_posts():
        return JobPost.query.all()