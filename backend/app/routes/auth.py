""" 
Handles Flask Dance routes for Google OAuth authentication
"""
from flask import Blueprint
from controllers.auth import AuthController

auth_routes = Blueprint('auth_routes', __name__, url_prefix='/auth')

# Google login route
@auth_routes.route('/login')
def google_login():
	return AuthController.google_login()
