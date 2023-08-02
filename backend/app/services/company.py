from models.company import Company
from models.user import User
from models.employer import Employer
from extensions import db
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity

class CompanyService:
	@staticmethod
	def get_profile(user_id):
		try:
			# Get employer's company id by user id
			user = Employer.query.filter_by(id=user_id).first()
			company_id = user.company_id
			if not company_id:
				return {'error': 'Company not found'}, 404
			# Get company by company id
			company = Company.query.filter_by(id=company_id).first()
			if company:
				return company.serialize()
			else:
				return {'error': 'Company not found'}, 404
		except Exception as e:
			print('Error: ', e)
			return {'error': str(e)}, 500
		
	@staticmethod
	@jwt_required()
	def update_profile(user_id, request):
		try:
			# Verify jwt token
			if not get_jwt_identity():
				return {'error': 'Unauthorized'}, 401
			user_email = get_jwt_identity()
			user = User.query.filter_by(email=user_email).first()
			# Check if user type is employer
			if user.type != 'employer':
				return {'error': 'Unauthorized'}, 401
			# Get employer's company id
			employer = Employer.query.filter_by(id=user_id).first()
			company_id = employer.company_id

			# Check if fields exist in request
			if 'name' in request.json:
				name = request.json['name']
			if 'description' in request.json:
				description = request.json['description']
			if 'website' in request.json:
				website = request.json['website']
			if 'industry' in request.json:
				industry = request.json['industry']
			if 'num_employees' in request.json:
				num_employees = request.json['num_employees']

			# If company id is not present then create it
			if not company_id:
				company = Company(name=name, description=description, website=website, industry=industry, num_employees=num_employees)
				db.session.add(company)
				db.session.commit()
				employer.company_id = company.id
				db.session.commit()
				return company.serialize()
			# If company id is present then update it
			else:
				company = Company.query.filter_by(id=company_id).first()
				company.name = name if name else company.name
				company.description = description if description else company.description
				company.website = website if website else company.website
				company.industry = industry if industry else company.industry
				company.num_employees = num_employees if num_employees else company.num_employees
				db.session.commit()
				return company.serialize()
		except Exception as e:
			print('Error: ', e)
			return {'error': str(e)}, 500

				
		
		
