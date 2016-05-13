import os

LOCAL_PSQLDB_URL = 'postgresql://project:project@localhost/dls'


class Config(object):
    DEBUG = True
    CSRF_ENABLED = True
    SECRET_KEY = 'asdk23akdskdsaasd'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.sqlite3'


class LocalConfig(Config):
    SQLALCHEMY_DATABASE_URI = LOCAL_PSQLDB_URL


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', LOCAL_PSQLDB_URL)


class HerokuConfig(ProductionConfig):
    DEBUG = True


class SQLiteConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.sqlite3'
