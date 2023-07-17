""" 
Handles Flask Dance routes for Google OAuth authentication
"""
from flask import Blueprint, redirect, request
from controllers.auth import AuthController
from flask_jwt_extended import jwt_required
from os import getenv

auth_routes = Blueprint('auth_routes', __name__, url_prefix='/auth')

# Google login route
@auth_routes.route('/login')
def google_login():
	return AuthController.google_login()

# Google login callback route
@auth_routes.route('/login/callback')
def google_login_callback():
	return AuthController.google_login_callback()

# Return user data
@auth_routes.route('/user')
@jwt_required()
def user():
	print('Request to /user')
	return AuthController.user_data()
