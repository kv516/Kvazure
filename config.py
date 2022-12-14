import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'kishoretsserver.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'kishoredb'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'kishoreadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Summer@123456'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'kishstorage'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'c/OgJ0YljdIqnQVj/p7fr6FiHpOLvBA8kaK8NkK7hkANn7vwdY9xwgWKo/qDaVJB+5EOUW4CYGR2+ASt0gpbDQ=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
