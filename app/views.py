from flask import render_template
from app import app
from .request import get_quote


@app.route('/')
def index():
  '''
  View root page function that returns the index page and its data
  '''
  
  quote = get_quote()
  title = "Personal Blog"
  return render_template('index.html', quote=quote, title=title)

  
@app.route('/blog/<int:id>')
def blog(id):
  '''
  View blog page function that returns the blog details page and its data
  '''
  return render_template('blog.html', id=id)


