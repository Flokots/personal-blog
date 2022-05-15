from app import app
import urllib.request, json
from .models import quote

Quote = quote.Quote

# Getting api key
base_url = app.config['QUOTES_BASE_URL']


def get_quote():
  '''
  Function that gets the json response to our url request
  '''
  get_quote_url= base_url

  with urllib.request.urlopen(get_quote_url) as url:
    get_quote_data = url.read()
    quote_response = json.loads(get_quote_data)
    if quote_response:
      author = quote_response.get("author")
      id = quote_response.get("id")
      quote = quote_response.get("quote")
      permalink = quote_response.get("permalink")

      quote_object = Quote(author, id, quote, permalink)
  return quote_object



 



