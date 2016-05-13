import os


class Config(object):
    DEBUG = True
    CSRF_ENABLED = True
    SECRET_KEY = 'asdk23akdskdsaasd'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.sqlite3'


class LocalConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://project:project@localhost/dls'


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class HerokuConfig(ProductionConfig):
    #SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/dls'
    pass


class SQLiteConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.sqlite3'
