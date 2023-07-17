from flask import redirect, jsonify
from services.auth import AuthService

class AuthController:		
	def google_login():
		try:
			# Return authservice redirect if it is a url
			response = AuthService.google_login()
			if response.startswith('http'):
				return redirect(response)
			# Return error if it is not a url
			else:
				jsonify(response)
		except Exception as e:
			return {'error': str(e)}, 500
		
	def user_data():
		try:
			return AuthService.user_data()
		except Exception as e:
			return {'error': str(e)}, 500
