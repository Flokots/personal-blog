from flask import render_template, redirect, url_for, abort
from flask_login import login_required

from . import main
from ..requests import get_quote
from ..models import Quote, User
from .forms import UpdateProfile
from .. import db


@main.route('/')
def index():
  '''
  View root page function that returns the index page and its data
  '''
  
  quote = get_quote()
  title = "Personal Blog"
  return render_template('index.html', quote=quote, title=title)


@main.route('/about')
def about():
  '''
  View page function that returns the about page and its data
  '''
  title = "About"
  return render_template('about.html', title=title)


@main.route('/contact')
def contact():
  '''
  View page function that returns the contact page and its data
  '''
  title = "Contact"
  return render_template('contact.html', title=title)


@main.route('/blog/<int:id>')
def blog(id):
  '''
  View blog page function that returns the blog details page and its data
  '''
  return render_template('blog.html', id=id)


@main.route('/user/<uname>')
def profile(uname):
  user = User.query.filter_by(username=uname).first()

  if user is None:
    abort(404)
  
  return render_template('profile/profile.html', user=user)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
  user = User.query.filter_by(username=uname).first()
  if user is None:
    abort(404)
  
  form = UpdateProfile()

  if form.validate_on_submit():
    user.bio = form.bio.data

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('.profile', uname=user.username))
  return render_template('profile/update.html', form=form)