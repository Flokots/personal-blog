from flask import render_template
from flask_login import login_required

from . import main
from ..requests import get_quote
from ..models import Quote


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


