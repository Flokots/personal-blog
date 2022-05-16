import os

class Config:
  '''
  General configuration parent class
  '''
  QUOTES_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://flo:flo@localhost:5433/personal_blog'
  SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
  '''
  Production configuration child class

  Args:
    Config: The parent configuration class with General Configuration settings
  '''
  pass


class DevConfig(Config):
  '''
  Development configuration child class

  Args:
    Config: The parent configuration class with General Configuration settings
  '''

  DEBUG = True

config_options = {
  'development': DevConfig,
  'production': ProdConfig
}

