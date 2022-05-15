import unittest
from models import quote
Quote = quote.Quote

class QuoteTest(unittest.TestCase):
  '''
  Test Class to test the behaviour of the Quote Class
  '''

  def setUp(self):
    '''
    Set up method that will run before every Test
    '''
    self.new_quote = Quote("Bill Gates", 6, "Measuring programming progress by lines of code is like measuring aircraft building progress by weight.", "http://quotes.stormconsultancy.co.uk/quotes/6")

  
  def test_instance(self):
    self.assertTrue(isinstance(self.new_quote, Quote))


  def test_init(self):
    '''
    test_init test case to test if the object is initialized properly.
    '''
    self.assertEqual(self.new_quote.author, "Bill Gates")
    self.assertEqual(self.new_quote.id, 6)
    self.assertEqual(self.new_quote.quote, "Measuring programming progress by lines of code is like measuring aircraft building progress by weight.")
    self.assertEqual(self.new_quote.permalink, "http://quotes.stormconsultancy.co.uk/quotes/6")
  
  


if __name__ == '__main__':
  unittest.main()