from services.job_post_service import JobPostService

def test_get_job_posts():
	job_posts = JobPostService.get_job_posts()
	assert job_posts is not None or len(job_posts) > 0

def test_get_job_post():
	job_post = JobPostService.get_job_post(1)
	assert job_post is not None
