from flask import Blueprint,request,flash,redirect,url_for,render_template
from .models import User
from flask_login import login_required,logout_user,login_user,current_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        email = request.form.get('email')
        
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first();
        if user and user.email!='':
            if check_password_hash(user.password,password):
                flash('Login successful',category='success')
                login_user(user,remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Wrong password. Try again!",category='error')
        else:
            flash('Invalid credentials.',category='error')

    return render_template('login.html',user = current_user)

@auth.route('/signup',methods=['POST','GET'])
def signup():
    if request.method=='POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password = request.form.get('password1')
        password2 = request.form.get('password2')
        if(password!=password2):
            flash("Passwords don't match",category='error')
        user = User.query.filter_by(email = email).first()
        if(user):
            flash("You are already registered")
            return redirect(url_for('auth.login'))
        new_user = User(email = email,first_name=first_name,password = generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user,remember=True)
        flash('account created',category='success')
        return redirect(url_for('views.home'));
    return render_template('signup.html',user = current_user);

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
