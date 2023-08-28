# -------------- IMPORTING THE REQUIRED MODULES --------------- #
import os
from dotenv import load_dotenv
load_dotenv()

# -------------- PATH OF BASE DIRECTORY --------------- #
CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
BASEDIR = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))


# -------------- CONFIGURATION CLASSES --------------- #
class Config():
    """
    Base class for some common configurations of the Flask App.
    """
    CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
    BASEDIR = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
    DEBUG = False
    SQLITE_DB_DIR = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False
    SECURITY_LOGIN_USER_TEMPLATE = "security/login_user.html"

class LocalDevelopmentConfig(Config):
    """
    Class for some common configurations of the Flask App related to Local Development.
    """

    ##### Flask APP Config #####
    DEBUG = True

    ##### Database Config #####
    SQLITE_DB_DIR = os.path.join(CURRENT_DIR, '../database')
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(SQLITE_DB_DIR, "QuantifiedSelfDevelopment.sqlite3")

    ##### Flask Security Config #####
    SECRET_KEY = os.getenv('SECRET_KEY') # Used for token generation
    SECURITY_PASSWORD_HASH = os.getenv('SECURITY_PASSWORD_HASH') # Hashing Algorithm
    SECURITY_PASSWORD_SALT = os.getenv('SECURITY_PASSWORD_SALT') # Used for hashing passwords
    SECURITY_REGISTERABLE = False
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_UNAUTHORIZED_VIEW = None # If one goes to an undefined url, it will through the default 404 error
    SECURITY_CONFIRMABLE = True
    SECURITY_AUTO_LOGIN_AFTER_CONFIRM = False
    SECURITY_RECOVERABLE = True
    SECURITY_POST_RESET_VIEW = '/recovered'

    ##### Flask Mail Config #####
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = os.getenv('MAIL_PORT')
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')

    ##### Flask Caching Config #####
    CACHE_TYPE = 'RedisCache'
    CACHE_REDIS_URL = os.getenv('REDIS_URL')
    CACHE_DEFAULT_TIMEOUT = 300 # 5 min default timeout
    CACHE_KEY_PREFIX = 'Track_it-'

    ##### Celery Config #####
    BROKER = os.getenv('REDIS_URL')
    BACKEND = os.getenv('REDIS_URL')
    ENABLE_UTC = False
    TIMEZONE = "Asia/Calcutta"

    
    
    
class ProductionConfig(Config):
    """
    Class for some common configurations of the Flask App related to Production.
    """

    ##### Database Config #####
    SQLITE_DB_DIR = os.path.join(BASEDIR, '../database')
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(SQLITE_DB_DIR, "QuantifiedSelfProduction.sqlite3")

    ##### Flask Security Config #####
    SECRET_KEY = os.getenv('SECRET_KEY') # Used for token generation
    SECURITY_PASSWORD_HASH = os.getenv('SECURITY_PASSWORD_HASH') # Hashing Algorithm
    SECURITY_PASSWORD_SALT = os.getenv('SECURITY_PASSWORD_SALT') # Used for hashing passwords
    SECURITY_REGISTERABLE = False
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_UNAUTHORIZED_VIEW = None # If one goes to an undefined url, it will through the default 404 error
    SECURITY_CONFIRMABLE = True
    SECURITY_AUTO_LOGIN_AFTER_CONFIRM = False
    SECURITY_RECOVERABLE = True
    SECURITY_POST_RESET_VIEW = '/recovered'

    ##### Flask Mail Config #####
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = os.getenv('MAIL_PORT')
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')

    ##### Flask Caching Config #####
    CACHE_TYPE = 'RedisCache'
    CACHE_REDIS_URL = os.getenv('REDIS_URL')
    CACHE_DEFAULT_TIMEOUT = 300 # 5 min default timeout
    CACHE_KEY_PREFIX = 'Track_it-'

    ##### Celery Config #####
    BROKER = os.getenv('REDIS_URL')
    BACKEND = os.getenv('REDIS_URL')
    ENABLE_UTC = False
    TIMEZONE = "Asia/Calcutta"




