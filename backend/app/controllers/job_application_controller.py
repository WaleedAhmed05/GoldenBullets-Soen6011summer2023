from services.job_application_service import JobApplicationService
from flask import jsonify

class JobApplicationController:
	def apply_job_post(request, id):
		try:
			job_post = JobApplicationService.apply_job_post(request, id)
			return jsonify(job_post)
		except Exception as e:
			return {'error': str(e)}, 500
		
	def get_job_post_applications(id):
		try:
			applications = jsonify(JobApplicationService.get_job_post_applications(id))
			return applications
		except Exception as e:
			return {'error': str(e)}, 500
		
	def get_job_post_application(job_id, application_id):
		try:
			application = jsonify(JobApplicationService.get_job_post_application(job_id, application_id))
			return application
		except Exception as e:
			return {'error': str(e)}, 500