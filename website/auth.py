from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from .models import User, JobPosting
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        role_option = request.form.get('role')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Set user role based on selected option
        if role_option == 'student':
            role = 'student'
        else:
            role = 'employer'

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, last_name=last_name, role=role, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()


            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)


@auth.route('/dashbord')
@login_required
def dashbord():
    joposting = None  # Initialize joposting variable
    is_new_job = True  # Set is_new_job to True since it's a new job posting

    return render_template('dashbord.html', user=current_user, joposting=joposting, is_new_job=is_new_job, header='Create A Job Posting')


@auth.route('/create_job', methods=['POST'])
def create_job():
    title = request.form.get('title')
    job_type = request.form.get('job-type')
    address = request.form.get('address')
    salary = float(request.form.get('salary'))
    # shift_schedule = ', '.join(request.form.getlist('shift-schedule'))
    # language = ', '.join(request.form.getlist('language'))
    description = request.form.get('description')
    requirements = request.form.get('requirements')

    job_posting = JobPosting(
        title=title,
        job_type=job_type,
        address=address,
        salary=salary,
        # shift_schedule=shift_schedule,
        # language=language,
        description=description,
        requirements=requirements,
        employer_id=current_user.id  # Set the relationship with the employer user
    )
    db.session.add(job_posting)
    db.session.commit()

    flash('Job posting created successfully!', category='success')
    return redirect(url_for('auth.dashbord'))

@auth.route('/managePosting')
@login_required
def manage_postings():
    jobpostings = JobPosting.query.filter_by(employer_id=current_user.id).all()
    return render_template('managePosting.html', jobpostings=jobpostings, user=current_user)




@auth.route('/view_job_posting/<int:job_id>')
@login_required
def view_job_posting(job_id):
    jposting = JobPosting.query.get_or_404(job_id)
    return render_template('view_job_posting.html', jposting=jposting, user=current_user)


@auth.route('/edit_job_posting/<int:job_id>', methods=['GET', 'POST'])
@login_required
def edit_job_posting(job_id):
    joposting = JobPosting.query.get_or_404(job_id)
    is_new_job = False

    if request.method == 'POST':
        if joposting.employer_id != current_user.id:
            flash('You do not have permission to edit this job posting.', category='error')
            return redirect(url_for('auth.manage_postings'))

        # Update the job posting fields based on the form data
        joposting.title = request.form.get('title')
        joposting.job_type = request.form.get('job-type')
        joposting.address = request.form.get('address')
        joposting.salary = float(request.form.get('salary'))
        joposting.description = request.form.get('description')
        joposting.requirements = request.form.get('requirements')

        db.session.commit()
        flash('Job posting updated successfully!', category='success')
        return redirect(url_for('auth.manage_postings'))

    return render_template('dashbord.html', joposting=joposting, user=current_user, is_new_job=is_new_job, header='Edit Job Posting', button_text='Update')



@auth.route('/Users')
def view_users():
    # Query all users from the database
    users = User.query.all()

    return render_template("Users.html", users=users)

@auth.route('/jobposted')
@login_required
def job_postings():
    job_postings = JobPosting.query.all()
    return render_template('jobposted.html', job_postings=job_postings)






