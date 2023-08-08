from flask import Flask
from flask_migrate import Migrate
from os import getenv, environ
from extensions import db
from dotenv import load_dotenv
from flask_dance.contrib.google import make_google_blueprint
from flask_jwt_extended import JWTManager, create_access_token
from flask_admin import Admin
from admin import init_admin, MyAdminIndexView
import logging

from routes.auth import auth_routes
from routes.job_post_routes import job_post_routes
from routes.candidate import candidate_routes
from routes.company import company_routes
from routes.browse_candidates_routes import browse_candidates_routes
from routes.job_search_routes import job_search_routes
from routes.notification import notification_routes
from routes.invite_candidates_routes import invite_candidate_routes
from routes.candidate_bookmark_routes import candidate_bookmark_routes
from routes.jobpost_bookmark_routes import jobpost_bookmark_routes
from routes.job_preferences_routes import candidate_jobpreferences_routes
from routes.alert_candidate_routes import alert_candidates_routes

load_dotenv('../.env', override=True)

# Set up Flask app
environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1' if getenv('FLASK_ENV') == 'development' else '0'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
app.config['JWT_SECRET_KEY'] = getenv('JWT_SECRET_KEY')

# Register extensions
ctx = app.app_context()
ctx.push()
with ctx:
	pass

db.init_app(app)
migrate = Migrate(app, db)
# Create database tables if they don't exist
with app.app_context():
	db.create_all()
	
# Set logging if in production
if getenv('FLASK_ENV') == 'production':
	logging.basicConfig(filename='app.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

# Set up Flask Dance routes
blueprint = make_google_blueprint(
    client_id = getenv('GOOGLE_CLIENT_ID'),
    client_secret = getenv('GOOGLE_CLIENT_SECRET'),
    scope = ['openid', 'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile'],
    redirect_url = '/auth/login/callback',
)

# Register routes
app.register_blueprint(auth_routes)
app.register_blueprint(job_post_routes)
app.register_blueprint(candidate_routes)
app.register_blueprint(company_routes)
app.register_blueprint(browse_candidates_routes)
app.register_blueprint(job_search_routes)
app.register_blueprint(notification_routes)
app.register_blueprint(invite_candidate_routes)
app.register_blueprint(candidate_bookmark_routes)
app.register_blueprint(jobpost_bookmark_routes)
app.register_blueprint(candidate_jobpreferences_routes)
app.register_blueprint(alert_candidates_routes)
app.register_blueprint(blueprint, url_prefix='/auth/login')

# Set up Flask Admin
admin = Admin(app, name='Concordia Career Services', template_mode='bootstrap3', index_view=MyAdminIndexView())
init_admin(admin, db)

# Set up JWT manager
jwt = JWTManager(app)

if __name__ == '__main__':
	# Set debug true if in development
	if getenv('FLASK_ENV') == 'development':
		app.debug = True
	app.run()
