from . import db


class Quote:
  '''
  Quote class to define quote objects
  '''

  def __init__(self, author, id, quote, permalink):
    self.author = author
    self.id = id
    self.quote = quote
    self.permalink = permalink


class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255), index=True)
  role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


  def __repr__(self):
    return f'{self.username}'
  


class Role(db.Model):
  __tablename__ = 'roles'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255))
  users = db.relationship('User', backref='role', lazy='dynamic')


  def __repr__(self):
    return f'{self.name}'