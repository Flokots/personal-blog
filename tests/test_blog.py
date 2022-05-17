import unittest
from app.models import Blog, User
from app import db

class TestBlog(unittest.TestCase):
  '''
  Test Class to test the behaviour of the Blog class
  '''

  def setUp(self):
    self.user_James = User(username='James', password='potato', email='james@ms.com', role='Admin')
    self.new_blog = Blog(id=1445, name="New blog", content="The newest content")

  
  def tearDown(self):
    Blog.query.delete()
    User.query.delete()

  
  def test_instance(self):
    self.assertTrue(isinstance(self.new_blog, Blog))

  
  def test_check_instance_variables(self):
    self.assertEquals(self.new_blog.name,"New blog" )
    self.assertEquals(self.new_blog.content, "The newest content")

  
  def test_save_blog(self):
    self.new_blog.save_blog()
    self.assertTrue(len(Blog.query.all())>0)
  

  def test_get_blogs(self):
    self.new_blog.save_blog()
    got_blogs = Blog.get_blogs()
    self.assertTrue(len(got_blogs) == 1)
