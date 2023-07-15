from flask import Blueprint, request, jsonify
from controllers.job_post_controller import JobPostController

job_post_routes = Blueprint('job_post_routes', __name__, url_prefix='/api/jobs')

@job_post_routes.route('/', methods=['GET'])
def get_job_posts():
	try:
		return JobPostController.get_job_posts()
	except Exception as e:
		return jsonify({'error': str(e)}), 500
	
@job_post_routes.route('/<int:id>', methods=['GET'])
def get_job_post(id):
	try:
		return JobPostController.get_job_post(id)
	except Exception as e:
		return jsonify({'error': str(e)}), 500