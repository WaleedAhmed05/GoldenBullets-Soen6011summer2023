from flask import Blueprint, request, jsonify
from controllers.filter_jobs_controller import FilterJobsController

filter_jobs_routes = Blueprint('filter_jobs_routes', __name__, url_prefix='/api/filter_jobs')

@filter_jobs_routes.route('/', methods=['GET'])
def get_filtered_jobs():
	try:
		return FilterJobsController.get_filtered_jobs()
	except Exception as e:
		return jsonify({'error': str(e)}), 500
