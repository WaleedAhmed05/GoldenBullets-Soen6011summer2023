from services.job_post_service import JobPostService

class JobPostController:
	def get_job_posts():
		try:
			job_posts = JobPostService.get_job_posts()
			return [job_post.serialize() for job_post in job_posts]
		except Exception as e:
			return {'error': str(e)}, 500
		
	def get_job_post(id):
		try:
			return JobPostService.get_job_post(id)
		except Exception as e:
			return {'error': str(e)}, 500