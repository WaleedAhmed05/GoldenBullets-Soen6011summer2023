from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from controllers.company import CompanyController

company_routes = Blueprint('company_routes', __name__, url_prefix='/api/company')

@jwt_required()
@company_routes.route('/<int:user_id>', methods=['PUT'])
def update_profile(user_id):
	try:
		return CompanyController.update_profile(user_id, request)
	except Exception as e:
		print('Error: ', e)
		return jsonify({'error': str(e)}), 500
	
@company_routes.route('/<int:user_id>', methods=['GET'])
def get_profile(user_id):
	try:
		return CompanyController.get_profile(user_id)
	except Exception as e:
		print('Error: ', e)
		return jsonify({'error': str(e)}), 500
	