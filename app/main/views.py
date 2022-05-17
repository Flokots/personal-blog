from crypt import methods
from flask import render_template, redirect, url_for, abort, request
from flask_login import login_required, current_user

from . import main
from ..requests import get_quote
from ..models import Quote, User, Blog, Comment
from .forms import UpdateProfile, AddBlog, CommentForm
from .. import db, photos


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
    user.role = "Writer"

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('.profile', uname=user.username))
  return render_template('profile/update.html', form=form)


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
  user = User.query.filter_by(username=uname).first()
  if 'photo' in request.files:
    filename = photos.save(request.files['photo'])
    path = f'photos/{filename}'
    user.profile_pic_path = path
    db.session.commit()
  return redirect(url_for('main.profile', uname=uname))



@main.route('/new/blog', methods=['GET', 'POST'])
@login_required
def new_blog():

  form = AddBlog()

  if form.validate_on_submit():
    user_id = current_user.id
    print(user_id)
    blog = Blog(name=form.name.data, content=form.content.data, user_id=user_id)
    db.session.add(blog)
    db.session.commit()

    name = form.name.data
    return redirect(url_for('main.blog', name=name))
  
  title="Add Blog"
  return render_template('new_blog.html', form=form, title=title)


@main.route('/blog/<int:blog_id>/comment', methods=['GET', 'POST'])
@login_required
def new_comment(blog_id):
  blog_id = blog_id
  form = CommentForm()
  if form.validate_on_submit():
    new_comment = Comment(name = form.name.data, blog_id=blog_id, user_id=current_user.id)
    db.session.add(new_comment)
    db.session.commit()

    blog= Blog.query.filter_by(id=blog_id).first()
    blog_name = blog.name
    
    
    return redirect(url_for('main.blog', name=blog_name))

  title="Comment"
  return render_template('new_comment.html', form=form, title=title)


@main.route('/blog/<name>')
def blog(name):
  '''
  View blog page function that returns the blog page details and its data
  '''
  blog = Blog.query.filter_by(name=name).first()
  comments = blog.comments
  return render_template('blog.html', blog=blog, comments=comments)

