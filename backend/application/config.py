# -------------- IMPORTING THE REQUIRED MODULES --------------- #
import os

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
    SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token"
    SECURITY_LOGIN_USER_TEMPLATE = "security/login_user.html"

class LocalDevelopmentConfig(Config):
    """
    Class for some common configurations of the Flask App related to Local Development.
    """

    SQLITE_DB_DIR = os.path.join(basedir, '../database')
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(SQLITE_DB_DIR, "QuantifiedSelfDevelopment.sqlite3")
    DEBUG = True
    # SECRET_KEY =  os.getenv("SECRET_KEY") # Used for token generation
    SECRET_KEY = "bnmvgd"
    SECURITY_PASSWORD_HASH = "bcrypt" # Hashing Algorithm
    # SECURITY_PASSWORD_SALT = os.getenv("SECURITY_PASSWORD_SALT") # Used for hashing passwords
    SECURITY_PASSWORD_SALT = "hdbksbviekensk"
    SECURITY_REGISTERABLE = False
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_UNAUTHORIZED_VIEW = None # If one goes to an undefined url, it will through the default 404 error
    
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


