from services.profile_edit_service import Profile_edit_service
from flask import jsonify


class profile_edit_controller:
    def upload_profile(id,cId,jobId, profile):  ##change into the controller names, not sure how to add into db
        Profile_edit_service.upload_profiles(id,cId,jobId,profile)
        return 'uploaded profile'

    def update_profile(cid,profile):
        Profile_edit_service.edit_profiles(cid, profile)
        return "updated"

    def get_profile(id):   #get profile by id
        try:
            profile = jsonify(Profile_edit_service.get_profiles(id))
            return profile
        except Exception as e:
            return {'error': str(e)}, 500