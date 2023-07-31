from flask_admin.contrib.sqla import ModelView
from models.user import User
from models.job_post import JobPost
from models.job_application import JobApplication
from models.company import Company

def init_admin(admin, db):
	admin.add_view(ModelView(User, db.session))
	admin.add_view(ModelView(JobPost, db.session))
	admin.add_view(ModelView(JobApplication, db.session))
	admin.add_view(ModelView(Company, db.session))
