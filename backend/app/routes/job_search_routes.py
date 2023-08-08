from flask import Blueprint, request, jsonify
from controllers.job_search import JobSearchController

job_search_routes = Blueprint('job_search_routes', __name__, url_prefix='/api/jobs/search')

@job_search_routes.route('/filter', methods=['GET'])
def filter_jobs():
	try:
		return JobSearchController.filter_jobs(request.args)
	except Exception as e:
		print('Error', e)
		return jsonify({'error': str(e)}), 500
	
@job_search_routes.route('/', methods=['GET'])
def search():
	try:
		return JobSearchController.search(request.args)
	except Exception as e:
		print('Error', e)
		return jsonify({'error': str(e)}), 500
	
@job_search_routes.route('/industries', methods=['GET'])
def list_all_industries():
	try:
		return JobSearchController.list_all_industries()
	except Exception as e:
		print('Error', e)
		return jsonify({'error': str(e)}), 500

