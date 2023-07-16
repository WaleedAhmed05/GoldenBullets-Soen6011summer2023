""" 
Handles Flask Dance routes for Google OAuth authentication
"""
from flask import Blueprint
from controllers.auth import AuthController
from flask_jwt_extended import jwt_required

auth_routes = Blueprint('auth_routes', __name__, url_prefix='/auth')

# Google login route
@auth_routes.route('/login')
def google_login():
	return AuthController.google_login()

# Return user data
@auth_routes.route('/user')
@jwt_required()
def user():
	print('Request to /user')
	return AuthController.user_data()
