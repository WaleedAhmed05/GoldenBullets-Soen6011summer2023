from services.company import CompanyService
from flask import jsonify

class CompanyController:
	def get_profile(user_id):
		try:
			company = jsonify(CompanyService.get_profile(user_id))
			return company
		except Exception as e:
			print('Error: ', e)
			return {'error': str(e)}, 500
		
	def update_profile(user_id, request):
		try:
			company = CompanyService.update_profile(user_id, request)
			return jsonify(company)
		except Exception as e:
			print('Error: ', e)
			return {'error': str(e)}, 500