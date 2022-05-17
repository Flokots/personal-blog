import unittest
from app.models import User, Comment, Blog
from app import db

class TestComment(unittest.TestCase):
  '''
  Test Class to test the behaviour of the Blog class
  '''

  def setUp(self):
    self.user_James = User(username='James', password='potato', email='james@ms.com', role='Admin')
    self.new_blog = Blog(id=12345, name="New blog", content="The newest content")
    self.new_comment = Comment(id=123456, name="New Comment")


  
  def tearDown(self):
    Blog.query.delete()
    User.query.delete()
    Comment.query.delete()

  
  def test_instance(self):
    self.assertTrue(isinstance(self.new_comment, Comment))

  
  def test_check_instance_variables(self):
    self.assertEquals(self.new_comment.name,"New Comment" )

  
  def test_save_comment(self):
    self.new_comment.save_comment()
    self.assertTrue(len(Comment.query.all())>0)
  
