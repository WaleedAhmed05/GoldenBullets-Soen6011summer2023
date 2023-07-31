from flask import Response
from os import getenv, environ
from dotenv import load_dotenv
from flask_admin import AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_httpauth import HTTPBasicAuth
from models.user import User
from models.job_post import JobPost
from models.job_application import JobApplication
from models.company import Company

auth = HTTPBasicAuth()

load_dotenv('../.env', override=True)

users = {
	getenv('ADMIN_USERNAME'): getenv('ADMIN_PASSWORD')
}

# Add authentication
@auth.verify_password
def verify_password(username, password):
	if username in users and password == users[username]:
		return username

class MyAdminIndexView(AdminIndexView):
	@expose('/')
	@auth.login_required
	def index(self):
		print(auth.current_user())
		return self.render('admin/index.html')

def init_admin(admin, db):
	admin.add_view(ModelView(User, db.session))
	admin.add_view(ModelView(JobPost, db.session))
	admin.add_view(ModelView(JobApplication, db.session))
	admin.add_view(ModelView(Company, db.session))