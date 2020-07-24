import os

class Config:
    '''
    General configuration parent class
    '''
    

    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://elly:Access2020@localhost/own_playlist"
    SECRET_KEY = os.environ.get('SECRET_KEY')


    UPLOADED_AUDIOS_DEST = 'app/static/audios'
class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://elly:Access2020@localhost/own_playlist"
    
class TestConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://elly:Access2020@localhost/own_playlist"
    

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
    Config: The parent configuration class with General configuration settings

    '''
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'testing' :TestConfig
}