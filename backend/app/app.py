from flask import Flask
from flask_migrate import Migrate
from os import getenv
from extensions import db
from dotenv import load_dotenv
import logging

load_dotenv('../.env', override=True)

# Set db connection
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Register extensions
db.init_app(app)
migrate = Migrate(app, db)
# Create database tables if they don't exist
with app.app_context():
	db.create_all()
	
# Set logging if in production
if getenv('FLASK_ENV') == 'production':
	logging.basicConfig(filename='app.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

# @todo: Register routes

if __name__ == '__main__':
	# Set debug true if in development
	if getenv('FLASK_ENV') == 'development':
		app.debug = True
	app.run()