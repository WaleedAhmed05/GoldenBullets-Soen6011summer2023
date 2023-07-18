"""
Handles Flask Dance routes for uploading and editing profiles
"""
from flask import Blueprint, request, jsonify
from controllers.profile_edit_controller import profile_edit_controller

#from flask_jwt_extended import jwt_required

profile_edit_routes = Blueprint('profile_edit_routes', __name__, url_prefix='/prof_edit')

@profile_edit_routes.route('/<int:id>/<int:cid>/<int:jobId>/<string:profile>', methods=['POST'])  # should be post
def upload_profile(id,cid,jobId,profile):  ###this method has some problems, probably in service
	profile_edit_controller.upload_profile(id, cid,jobId,profile)
	return jsonify({'success': "succeed"}), 100


@profile_edit_routes.route('/<int:cid>/<string:profile>', methods=['POST'])  #update, haven't tested yet
def edit_profile(cid,profile):
	profile_edit_controller.update_profile(cid,profile)
	return jsonify({'success': "succeed"}), 100

# Return user data
@profile_edit_routes.route('/<int:id>', methods=['GET'])  #"error": "'NoneType' object has no attribute 'serialize'"
def get_profile(id):
	try:
		return profile_edit_controller.get_profile(id)
	except Exception as e:
		return jsonify({'error': str(e)}), 500
