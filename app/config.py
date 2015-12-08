import os
from flask_appbuilder.security.manager import AUTH_OID, AUTH_REMOTE_USER, AUTH_DB, AUTH_LDAP, AUTH_OAUTH
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """SCHEDULER_JOBSTORES = {
        'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
    }"""
    SCHEDULER_EXECUTORS = {
        'default': ThreadPoolExecutor(20),
        'processpool': ProcessPoolExecutor(5)
    }
    SCHEDULER_DEFAULTS = {
        'coalesce': False,
        'max_instances': 3
    }
    # Your App secret key
    SECRET_KEY = '\2\1thisismyscretkey\1\2\e\y\y\h'

    # The SQLAlchemy connection string.
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    # SQLALCHEMY_DATABASE_URI = 'mysql://myapp@localhost/myapp'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://root:password@localhost/myapp'

    # Flask-WTF flag for CSRF
    CSRF_ENABLED = True

    # ------------------------------
    # GLOBALS FOR APP Builder
    # ------------------------------
    # Uncomment to setup Your App name
    APP_NAME = "Flower Master"

    # Uncomment to setup Setup an App icon
    # APP_ICON = "static/img/logo.jpg"

    # ----------------------------------------------------
    # AUTHENTICATION CONFIG
    # ----------------------------------------------------
    # The authentication type
    # AUTH_OID : Is for OpenID
    # AUTH_DB : Is for database (username/password()
    # AUTH_LDAP : Is for LDAP
    # AUTH_REMOTE_USER : Is for using REMOTE_USER from web server
    AUTH_TYPE = AUTH_DB

    # Uncomment to setup Full admin role name
    # AUTH_ROLE_ADMIN = 'Admin'

    # Uncomment to setup Public role name, no authentication needed
    # AUTH_ROLE_PUBLIC = 'Public'

    # Will allow user self registration
    # AUTH_USER_REGISTRATION = True

    # The default user self registration role
    # AUTH_USER_REGISTRATION_ROLE = "Public"

    # When using LDAP Auth, setup the ldap server
    # AUTH_LDAP_SERVER = "ldap://ldapserver.new"

    # Uncomment to setup OpenID providers example for OpenID authentication
    # OPENID_PROVIDERS = [
    #    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    #    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    #    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    #    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
    # ---------------------------------------------------
    # Babel config for translations
    # ---------------------------------------------------
    # Setup default language
    BABEL_DEFAULT_LOCALE = 'en'
    # Your application default translation path
    BABEL_DEFAULT_FOLDER = 'translations'
    # The allowed translation for you app
    LANGUAGES = {
        'en': {'flag': 'gb', 'name': 'English'},
    }
    # ---------------------------------------------------
    # Image and file configuration
    # ---------------------------------------------------
    # The file upload folder, when using models with files
    UPLOAD_FOLDER = basedir + '/app/static/uploads/'

    # The image upload folder, when using models with images
    IMG_UPLOAD_FOLDER = basedir + '/app/static/uploads/'

    # The image upload url, when using models with images
    IMG_UPLOAD_URL = '/static/uploads/'
    # Setup image size default is (300, 200, True)
    # IMG_SIZE = (300, 200, True)

    # Theme configuration
    # these are located on static/appbuilder/css/themes
    # you can create your own and easily use them placing them on the same dir structure to override
    APP_THEME = "bootstrap-theme.css"  # default bootstrap
    # APP_THEME = "cerulean.css"
    # APP_THEME = "amelia.css"
    # APP_THEME = "cosmo.css"
    # APP_THEME = "cyborg.css"
    # APP_THEME = "flatly.css"
    # APP_THEME = "journal.css"
    # APP_THEME = "readable.css"
    # APP_THEME = "simplex.css"
    # APP_THEME = "slate.css"
    # APP_THEME = "spacelab.css"
    # APP_THEME = "united.css"
    # APP_THEME = "yeti.css"
    EMAIL_URL = "florianhub.appspot.com/email"


class ProductionConfig(Config):
    HARDWARE = True
    TESTING = False
    HUB_URL = "http://florian-hub.appspot.com"


class DevelopmentConfig(Config):
    HARDWARE = False
    TESTING = False
    HUB_URL = "http://127.0.0.1:8080"


class TestingConfig(Config):
    HARDWARE = False
    TESTING = True
    HUB_URL = "http://127.0.0.1:8080"


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,

    'default': ProductionConfig,
}
