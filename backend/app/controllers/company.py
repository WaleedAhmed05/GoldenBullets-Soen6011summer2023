from services.company import CompanyService
from flask import jsonify

class CompanyController:
	def create_company(request):
		try:
			company = jsonify(CompanyService.create_company(request))
			return company
		except Exception as e:
			return {'error': str(e)}, 500
		
	def get_company(id):
		try:
			company = jsonify(CompanyService.get_company(id))
			return company
		except Exception as e:
			return {'error': str(e)}, 500