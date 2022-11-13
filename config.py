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
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '5P9s5a1NuF6PpmyrvL06Qtmd1aKST/1IaLgtScydCWRkC2NSjXFx1p9skYF5iuOzLAPEa/r2PEcH+AStvEwG0A=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
