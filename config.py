import os
DEBUG = True

SECRET_KEY = os.urandom(24)

DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'test'
PASSWORD = '123456'
HOST = '47.98.177.139'
PORT = '3306'
DATABASE = 'Test'

# 配置和数据库的连接信息
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://test:123456@47.98.177.139/Test'
SQLALCHEMY_TRACK_MODIFICATIONS = False