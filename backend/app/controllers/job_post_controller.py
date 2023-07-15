from services.job_post_service import JobPostService
from flask import jsonify

class JobPostController:
	def get_job_posts():
		try:
			job_posts = jsonify(JobPostService.get_job_posts())
			return job_posts
		except Exception as e:
			return {'error': str(e)}, 500
		
	def get_job_post(id):
		try:
			job_post = jsonify(JobPostService.get_job_post(id))
			return job_post
		except Exception as e:
			return {'error': str(e)}, 500