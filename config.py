import os

class Config:
  '''
  General configuration parent class
  '''
  QUOTES_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'


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

