from models.bookmark import Bookmark
from models.user import User
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import db

class JobpostBookmarkService:
        @staticmethod
        @jwt_required()
        def bookmark_jobpost(request):
            try:
                # Get user from jwt token
                user_email = get_jwt_identity()
                user = User.query.filter_by(email=user_email).first()
                # Check if user type is candidate
                if user.type != 'candidate':
                    return {'error': 'Unauthorized'}, 401
                
                job_id = request.json['job_id']
                candidate_id = request.json['candidate_id']

                prev_bookmarks = Bookmark.query.filter_by(employer_id = None,
                                                        candidate_id=candidate_id,
                                                        job_id=job_id ).first()
                if prev_bookmarks is None:
                    addbookmark = Bookmark(employer_id=None,
                                                        candidate_id=candidate_id,
                                                        job_id=job_id )
                    db.session.add(addbookmark)
                    db.session.commit()
                    return addbookmark.serialize(), 200
                else:
                    return {'error': 'Jobpost already bookmarked'}, 400
            except Exception as e:
                print('error', e)
                return {'error': str(e)}, 500