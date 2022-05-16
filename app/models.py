from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

from . import db
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class Quote:
  '''
  Quote class to define quote objects
  '''

  def __init__(self, author, id, quote, permalink):
    self.author = author
    self.id = id
    self.quote = quote
    self.permalink = permalink


class User(UserMixin, db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255), index=True)
  email = db.Column(db.String(255), unique=True, index=True)
  bio = db.Column(db.String(255))
  profile_pic_path = db.Column(db.String())
  role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
  blogs = db.relationship('Blog', backref = 'writer', lazy='dynamic')
  comments = db.relationship('Comment', backref = 'commenter', lazy='dynamic')
  pass_secure = db.Column(db.String(255))

  @property
  def password(self):
    raise AttributeError('You cannot read the password attribute')

  
  @password.setter
  def password(self, password):
    self.pass_secure = generate_password_hash(password)

  def verify_password(self, password):
    return check_password_hash(self.pass_secure, password)

  def __repr__(self):
    return f'{self.username}'
  


class Role(db.Model):
  '''
  Role class to define blog objects
  '''
  __tablename__ = 'roles'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255))
  users = db.relationship('User', backref='role', lazy='dynamic')

  def __repr__(self):
    return f'{self.name}'


class Blog(db.Model):
  '''
  Blog class to define blog objects
  '''
  __tablename__ = 'blogs'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  content = db.Column(db.Text, nullable=False)
  urlToImage = db.Column(db.String())
  posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  comments = db.relationship('Comment', backref = 'blog', lazy='dynamic')
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

  def save_blog(self):
    db.session.add(self)
    db.session.commit()
  
  @classmethod
  def get_blogs(cls):
    blogs = Blog.query.all()
    return blogs
  
  
  def __repr__(self):
    return f'{self.name}'


class Comment(db.Model):
  '''
  Comment class to define Comment Objects
  '''
  __tablename__ = 'comments'

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(255))
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
  posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


  def save_comment(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_comment(cls, id):
    comments = Comment.query.filter_by(blog_id = id).all()

    return comments

