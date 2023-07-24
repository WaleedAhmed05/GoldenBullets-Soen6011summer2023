from models.company import Company
from models.user import User
from models.employer import Employer
from extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity

class CompanyService:
	@staticmethod
	@jwt_required()
	def create_company(request):
		try:
			# Verify jwt token
			if not get_jwt_identity():
				return {'error': 'Unauthorized'}, 401
			# Get user email from jwt token
			user_email = get_jwt_identity()
			user = User.query.filter_by(email=user_email).first()
			# Check if user type is employer
			if user.type != 'employer':
				return {'error': 'Unauthorized'}, 401

			name = request.json['name']
			description = request.json['description']
			website = request.json['website']
			industry = request.json['industry']
			num_employees = request.json['num_employees']
			created_by = user.id
			company = Company(name=name, description=description, website=website, industry=industry, num_employees=num_employees, created_by=created_by)
			db.session.add(company)
			db.session.commit()
			# Update company id field in employer table
			employer = Employer.query.filter_by(id=user.id).first()
			employer.company_id = company.id
			db.session.commit()

			return company.serialize()
		except Exception as e:
			print('error', e)
			return {'error': str(e)}, 500

	@staticmethod
	def get_company(id):
		try:
			company = Company.query.get(id)
			return company.serialize()
		except Exception as e:
			return {'error': str(e)}, 500


