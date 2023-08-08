from services.job_post_service import JobPostService
from flask import jsonify

class JobPostController:
	def get_job_posts():
		try:
			job_posts = jsonify(JobPostService.get_job_posts())
			return job_posts
		except Exception as e:
			return {'error': str(e)}, 500

	# Retrieve all job posts by a specific employer
	def get_employer_job_posts():
		try:
			job_posts = jsonify(JobPostService.get_employer_job_posts())
			return job_posts
		except Exception as e:
			return {'error': str(e)}, 500
	# Retrieve a specific job post based on the provided 'id'	
	def get_job_post(id):
		try:
			job_post = jsonify(JobPostService.get_job_post(id))
			return job_post
		except Exception as e:
			return {'error': str(e)}, 500
		
	def create_job_post(request):
		try:
			job_post = JobPostService.create_job_post(request)
			return jsonify(job_post)
		except Exception as e:
			return {'error': str(e)}, 500
		
	def update_job_post(request, id):
		try:
			job_post = JobPostService.update_job_post(request, id)
			return jsonify(job_post)
		except Exception as e:
			return {'error': str(e)}, 500

