from flask import render_template, request, redirect, session, flash
from config import app, db, bcrypt
from models import User
from datetime import date, time
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def main():
    print("*"*40)
    return render_template("selectors.html")

def color():
    return render_template("animation.html")

def add_user():
    if len(request.form['fname'])<2:
        flash("First name is required")
    if len(request.form['lname'])<2:
        flash("Last name is required")
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Valid email is required")   
    if len(request.form['password']) < 5:
        flash("password isn't long enough")
    if request.form['password'] != request.form['cpassword']:
        flash("password dont match")
    if '_flashes' not in session:
        new_user = User(
            first_name = request.form['fname'],
            last_name = request.form['lname'],
            email = request.form['email'],
            password_hash=bcrypt.generate_password_hash(request.form['password']))   
        db.session.add(new_user)
        db.session.commit()
        flash("Successfully added user")
        return redirect("/")
    return redirect('/')   
        

def login():
    is_valid = True
    if len(request.form['email']) < 1:
        is_valid = False
        flash("Email is required")
    if len(request.form['password']) < 1:
        is_valid = False
        flash("Password is required")

    if is_valid:
        user = User.query.filter_by(email=request.form['email']).all()
        if user:
            if bcrypt.check_password_hash(user[0].password_hash, request.form['password']):
                session['user_id'] = user[0].id
                return redirect("/user_page")
            else:
                flash("Email and/or password do not match")
        else:
                flash("Email and/or password do not match")
    return redirect("/")

def logout():
    session.clear()
    return redirect("/")