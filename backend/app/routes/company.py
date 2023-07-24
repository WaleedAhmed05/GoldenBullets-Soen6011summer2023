""" 
Handles all routes related to company
"""
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from controllers.company import CompanyController

company_routes = Blueprint('company_routes', __name__, url_prefix='/api/company')

# Create company route
@company_routes.route('/', methods=['POST'])
@jwt_required()
def create_company():
	try:
		return CompanyController.create_company(request)
	except Exception as e:
		return jsonify({'error': str(e)}), 500
	
# Get company route
@company_routes.route('/', methods=['GET'])
def get_company():
	try:
		return CompanyController.get_company()
	except Exception as e:
		return jsonify({'error': str(e)}), 500
