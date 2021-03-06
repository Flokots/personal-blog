from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required

from ..models import User, Blog
from .forms import LoginForm, RegistrationForm, SubscriptionForm
from ..email import mail_message
from .. import db
from . import auth
import email

@auth.route('/login', methods=['GET', 'POST'])
def login():
  login_form = LoginForm()
  if login_form.validate_on_submit():
    user = User.query.filter_by(email=login_form.email.data).first()
    if user is not None and user.verify_password(login_form.password.data):
      login_user(user, login_form.remember.data)
      return redirect(request.args.get('next') or url_for('main.index'))

    flash('Invalid username or Password')

  title = "Personal Blog Login"
  return render_template('auth/login.html', login_form=login_form, title=title)


@auth.route('/register', methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    role = "Author"
    user = User(email=form.email.data, username=form.username.data, password=form.password.data, role=role)
    db.session.add(user)
    db.session.commit()

    mail_message("Welcome to The Nightngale Personal Blog", "email/welcome_user", user.email, user=user)

    return redirect(url_for('auth.login'))
  title = "New Account"
  return render_template('auth/register.html', registration_form = form, title=title)


@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('main.index'))


@auth.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
  form = SubscriptionForm()

  if form.validate_on_submit():
    user=User(email=form.email.data, username=form.username.data, role="Subscriber")
    db.session.add(user)
    db.session.commit()
    mail_message("Thank you for subscribing to The Nightngale Personal Blog", "email/thank_you", user.email, user=user)
    flash('Subscription successful')
  title='Subscribe'
  return render_template('auth/subscribe.html', form=form, title=title)


@auth.route('/new/post/<name>', methods=['GET', 'POST'])
def post_notification(name):
    users = User.query.filter_by(role="Subscriber").all()
    name=name
    
    if users:
      for user in users:
        email=user.email
        mail_message("New Post Alert", "email/new_post", email, name=name, user=user)
  
    return redirect(url_for('main.index'))

