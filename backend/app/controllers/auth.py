from flask import redirect, jsonify
from services.auth import AuthService

# Defining the AuthController class responsible for handling authentication operations
class AuthController:
	# Initiating Google login
	def google_login():
		try:
			# Redirect to google login
			url = AuthService.google_login()
			return redirect(url)
		except Exception as e:
			return {'error': str(e)}, 500
	
	def google_login_callback():
		try:
			# Return authservice redirect if it is a url
			response = AuthService.google_login_callback()
			# If response is string, redirect. Else return response
			if isinstance(response, str):
				return redirect(response)
			else:
				return response
		except Exception as e:
			return {'error': str(e)}, 500
		
	def user_data():
		try:
			# Retrieve user data from the AuthService
			return AuthService.user_data()
		except Exception as e:
			return {'error': str(e)}, 500
