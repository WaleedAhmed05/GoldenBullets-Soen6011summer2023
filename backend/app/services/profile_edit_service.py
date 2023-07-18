from models.candidate import Candidate


class Profile_edit_service:
    @staticmethod
    def upload_profiles(id,cId,jobId, profile):
        newProfile = Candidate(id,profile,cId,jobId)  #didn't commit to the actual db
        #newProfile.save()   #not sure if this part works
        return 1
        #return [job_post.serialize() for job_post in job_posts]

    #db.session.add(Staff(request.form['theUsername'], generate_password_hash(request.form['password'])))
    #db.session.commit()

    @staticmethod
    def edit_profiles(id,profile):#not sure about save updates here
        mycand = Candidate.query.get(id).changeProf(profile)
        return mycand.serialize()#Candidate.query.get(id).serialize()

    @staticmethod
    def get_profiles(id):
        return Candidate.query.get(id).serialize()