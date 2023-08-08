from models.job_preferences import JobPreferences
from models.user import User
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import db


class SetJobPreferenceService:
        @staticmethod
        # @jwt_required()
        def set_job_preference(request):
            try:
                # # Get user from jwt token
                # user_email = get_jwt_identity()
                # user = User.query.filter_by(email=user_email).first()
                # # Check if user type is candidate
                # if user.type != 'candidate':
                #     return {'error': 'Unauthorized'}, 401

                fcandidate_id = request.json['candidate_id']
                ftitle = request.json['title']
                flocation = request.json['location']
                fjob_type = request.json['job_type']

                prev_preferences = JobPreferences.query.filter_by(candidate_id=fcandidate_id,
                                                                    title=ftitle,
                                                                    location=flocation,
                                                                    job_type=fjob_type).first()

                if prev_preferences is None:
                    addprefernce = JobPreferences(candidate_id=fcandidate_id,
                                                    title=ftitle,
                                                    location=flocation,
                                                    job_type=fjob_type)
                    db.session.add(addprefernce)
                    db.session.commit()
                    return addprefernce.serialize(), 200
                else:
                    return {'error': 'Job Preference with given filters already exists'}, 400
            except Exception as e:
                print('error', e)
                return {'error': str(e)}, 500