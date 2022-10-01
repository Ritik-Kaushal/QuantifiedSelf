# -------------- IMPORTING THE REQUIRED MODULES --------------- #
import os

from sqlalchemy import true

# -------------- PATH OF BASE DIRECTORY --------------- #
basedir = os.path.abspath(os.path.dirname(__file__)) # path of the base directory
# It looks something like this => 'C:\\Users\\ritik\\Desktop\\QuantifiedSelf-II\\backend'

# -------------- CONFIGURATION CLASSES --------------- #
class Config():
    """
    Base class for some common configurations of the Flask App.
    """

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
    SQLITE_DB_DIR = os.path.join(basedir, '../database')
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(SQLITE_DB_DIR, "QuantifiedSelfDevelopment.sqlite3")

    ##### Flask Security Config #####
    SECRET_KEY = "bnmvgd" # Used for token generation
    SECURITY_PASSWORD_HASH = "bcrypt" # Hashing Algorithm
    SECURITY_PASSWORD_SALT = "hdbksbviekensk" # Used for hashing passwords
    SECURITY_REGISTERABLE = False
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_UNAUTHORIZED_VIEW = None # If one goes to an undefined url, it will through the default 404 error
    SECURITY_CONFIRMABLE = True
    SECURITY_AUTO_LOGIN_AFTER_CONFIRM = False
    SECURITY_RECOVERABLE = True
    SECURITY_POST_RESET_VIEW = '/recovered'

    ##### Flask Mail Config #####
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = '465'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = "emailinflaskbyritik@gmail.com"
    MAIL_PASSWORD = "podhjstbwoaxxjoc"

    ##### Flask Caching Config #####
    CACHE_TYPE = 'RedisCache'
    CACHE_REDIS_URL = 'redis://localhost:6379/0'
    CACHE_DEFAULT_TIMEOUT = 300 # 5 min default timeout
    CACHE_KEY_PREFIX = 'Track_it-'

    ##### Celery Config #####
    BROKER = "redis://localhost:6379/0"
    BACKEND = "redis://localhost:6379/0"
    ENABLE_UTC = False
    TIMEZONE = "Asia/Calcutta"

    
    
    
class ProductionConfig(Config):
    """
    Class for some common configurations of the Flask App related to Production.
    """

    SQLITE_DB_DIR = os.path.join(basedir, '../database')
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(SQLITE_DB_DIR, "QuantifiedSelfProduction.sqlite3")
    SECRET_KEY =  os.getenv("SECRET_KEY") # Used for token generation
    SECURITY_PASSWORD_HASH = "bcrypt" # Hashing Algorithm
    SECURITY_PASSWORD_SALT = os.getenv("SECRET_SALT") # Used for hashing passwords
    SECURITY_REGISTERABLE = True
    SECURITY_CONFIRMABLE = False
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_UNAUTHORIZED_VIEW = None # If one goes to an undefined url, it will through the default 404 error


