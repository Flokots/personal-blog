import email
import unittest
from app.models import User

class UserModelTest(unittest.TestCase):

  def setUp(self):
    self.new_user = User(id=12345, password= 'banana', username='ndizi', email='ndizi@gmail.com', bio='hey world', profile_pic_path='/static/photos/star.jpg')
  
  def tearDown(self):
    User.query.delete()

  def test_password_setter(self):
    self.assertTrue(self.new_user.pass_secure is not None)

  def test_no_access_password(self):
    with self.assertRaises(AttributeError):
      self.new_user.password

  def test_password_verification(self):
    self.assertTrue(self.new_user.verify_password('banana'))

  def test_init(self):
    '''
    test_init test case to test if the object is initialized properly.
    '''
    self.assertEqual(self.new_user.id, 12345)
    self.assertEqual(self.new_user.username, 'ndizi')
    self.assertEqual(self.new_user.email, 'ndizi@gmail.com')
    self.assertEqual(self.new_user.bio, 'hey world')
    self.assertEqual(self.new_user.profile_pic_path, '/static/photos/star.jpg')