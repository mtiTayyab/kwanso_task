import os


class Config(object):
    ENV = "developement"
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # DB Credentials
    host = 'localhost'
    db = 'kwanso_task_db'
    user = 'tayiqb'
    password = 'refill'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + user + ':' + password + '@' + host + '/' + db + '?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'aA3sda!d4453FFS1SN231lLso342n!SS2A192'

    MYSQL_DATABASE_HOST = host
    MYSQL_DATABASE_USER = user
    MYSQL_DATABASE_PASSWORD = password
    MYSQL_DATABASE_DB = db
