from flask import render_template
from app import app


@app.route('/')
def index():
  '''
  View root page function that returns the index page and its data
  '''
  return render_template('index.html')

  
@app.route('/blog/<int:id>')
def blog(id):
  '''
  View blog page function that returns the blog details page and its data
  '''
  return render_template('blog.html', id=id)


