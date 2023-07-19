from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from controllers.job_post_controller import JobPostController

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