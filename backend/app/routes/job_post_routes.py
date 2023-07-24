from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from controllers.job_post_controller import JobPostController
from controllers.job_application_controller import JobApplicationController

job_post_routes = Blueprint('job_post_routes', __name__, url_prefix='/api/jobs')

@job_post_routes.route('/', methods=['GET'])
def get_job_posts():
	try:
		return JobPostController.get_job_posts()
	except Exception as e:
		return jsonify({'error': str(e)}), 500
	
@jwt_required()
@job_post_routes.route('/employer', methods=['GET'])
def get_employer_job_posts():
	try:
		return JobPostController.get_employer_job_posts()
	except Exception as e:
		return jsonify({'error': str(e)}), 500
	
@job_post_routes.route('/<int:id>', methods=['GET'])
def get_job_post(id):
	try:
		return JobPostController.get_job_post(id)
	except Exception as e:
		return jsonify({'error': str(e)}), 500
	
@jwt_required()
@job_post_routes.route('/', methods=['POST'])
def create_job_post():
	try:
		return JobPostController.create_job_post(request)
	except Exception as e:
		return jsonify({'error': str(e)}), 500
	
@jwt_required()
@job_post_routes.route('/<int:id>', methods=['PUT'])
def update_job_post(id):
	try:
		return JobPostController.update_job_post(id, request)
	except Exception as e:
		return jsonify({'error': str(e)}), 500
	
@jwt_required()
@job_post_routes.route('/<int:id>/apply', methods=['POST'])
def apply_job_post(id):
	try:
		return JobApplicationController.apply_job_post(id, request)
	except Exception as e:
		return jsonify({'error': str(e)}), 500
	
@jwt_required()
@job_post_routes.route('/<int:id>/applications', methods=['GET'])
def get_job_post_applications(id):
	try:
		return JobApplicationController.get_job_post_applications(id)
	except Exception as e:
		return jsonify({'error': str(e)}), 500
	
@jwt_required()
@job_post_routes.route('/<int:job_id>/applications/<int:application_id>', methods=['GET'])
def get_job_post_application(job_id, application_id):
	try:
		return JobApplicationController.get_job_post_application(job_id, application_id)
	except Exception as e:
		return jsonify({'error': str(e)}), 500
	
@jwt_required()
@job_post_routes.route('/applications/<int:application_id>', methods=['PUT'])
def update_job_post_application(application_id):
	try:
		return JobApplicationController.update_job_post_application(application_id, request)
	except Exception as e:
		print('error', e)
		return jsonify({'error': str(e)}), 500
