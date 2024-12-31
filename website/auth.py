# from flask import Blueprint , render_template ,request,flash,redirect,url_for
# from .models import User
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import login_user,login_required ,logout_user, current_user

# from .import db

# auth = Blueprint('auth',__name__)

# @auth.route('/login' ,methods=['GET','POST'])
# def login(): 
#     if request.method=="POST":
#         email=request.form.get('email')
#         password=request.form.get('password')
#         user =User.query.filter_by(email=email).first()
#         if not email or not password:
#             flash('All fields must be finished ',category='error')
#         elif user:
#             if check_password_hash(user.password ,password):
#                 login_user(user , remember=True)
#                 flash("Login successfull",category="success")
#             else: 
#                 flash("Incorrect password",category="error")
#         else:
#             flash("No User Exists with this Email ", category="error")
#     return render_template('login.html',user=current_user)

# @auth.route('/log_out') 
# @login_required
# def log_out():
#     login_user()
#     return redirect(url_for("auth.login"))

# @auth.route('/sign_up' ,methods=['GET','POST'])
# def sign_up():
#     if request.method=="POST":
#         username=request.form.get('username')
#         email=request.form.get('email')
#         password=request.form.get('password')
#         user =User.query.filter_by(email=email).first()
#         if user:
#             flash("User already exists",category='error')
#         if not password or not username or not email:
#             flash(" All fields must be FILLED !",category="error")
#         else:
#             new_user=User(email=email,
#                           username=username,
#                           password=generate_password_hash(password,  method='pbkdf2:sha256'))
#             db.session.add(new_user)
#             db.session.commit()
#             login_user(user , remember=True)
#             flash("Account Created Successfully",category="sucess")
#             return redirect(url_for('views.login'))
#     return render_template('sign_up.html',user=current_user) 

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
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


@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif not username or not email or not password:
            flash('All fields must be filled',category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(
                password, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)