from flask import Blueprint, jsonify, request
from controllers.job_post_controller import JobPostController

job_post_routes = Blueprint('job_post_routes', __name__, url_prefix='/api/jobs')

@job_post_routes.route('/', methods=['GET'])
def get_job_posts():
	try:
		job_posts = JobPostController.get_job_posts()
		return jsonify(job_posts)
	except Exception as e:
		return jsonify({'error': str(e)}), 500