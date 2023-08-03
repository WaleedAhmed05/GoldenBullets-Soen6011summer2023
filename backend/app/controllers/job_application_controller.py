from services.job_application_service import JobApplicationService
from flask import jsonify

# Handling job application operations
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
	# Retrieve a specific job application for a job post based on the provided 'job_id' and 'application_id'	
	def get_job_post_application(job_id, application_id):
		try:
			application = jsonify(JobApplicationService.get_job_post_application(job_id, application_id))
			return application
		except Exception as e:
			return {'error': str(e)}, 500

	# Update the status of a job application based on the provided 'application_id' and 'request' object
	def update_job_post_application(application_id, request):
		try:
			status = request.get_json()['status']
			if status == 'interview':
				interview = request.get_json()['invite']
				return JobApplicationService.set_job_application_interview(application_id, status, interview)
			return JobApplicationService.update_job_post_application(application_id, status)
		except Exception as e:
			print('error', e)
			return {'error': str(e)}, 500
		
	def get_applications_by_candidate():
		try:
			return JobApplicationService.get_applications_by_candidate()
		except Exception as e:
			print('error', e)
			return {'error': str(e)}, 500

	def get_job_application_interview(job_id, application_id):
		try:
			application = jsonify(JobApplicationService.get_job_application_interview(job_id, application_id))
			return application
		except Exception as e:
			return {'error': str(e)}, 500

	def set_job_application_interview(application_id, request):
		try:
			interview = request.get_json()
			return JobApplicationService.set_job_application_interview(application_id, interview)
		except Exception as e:
			print('error', e)
			return {'error': str(e)}, 500
