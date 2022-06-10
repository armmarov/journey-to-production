import os

basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'TestServer123')
    JWT_SECRET_KEY = "TEST_SECURITY"
    JWT_HEADER_NAME = "Authorization"
    JWT_HEADER_TOKEN_PREFIX = ""
    REFRESH_EXP_LENGTH = 30
    ACCESS_EXP_LENGTH = 10


class DevelopmentConfig(BaseConfig):
    FLASK_ENV = 'development'
    DBNAME = 'testdb'
    SQLALCHEMY_DATABASE_URI = basedir + "/app_dev.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SWAGGER = {
        'title': 'Development Server',
    }


class StagingConfig(BaseConfig):
    FLASK_ENV = 'staging'
    DBNAME = 'testdb'
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = basedir + "/app_stage.db"
    SWAGGER = {
        'title': 'Staging Server',
    }


class ProductionConfig(BaseConfig):
    FLASK_ENV = 'production'
    DBNAME = 'testdb'
    SQLALCHEMY_DATABASE_URI = basedir + "/app_prod.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER = {
        'title': 'Production Server',
    }


config_by_name = dict(
    dev=DevelopmentConfig,
    stage=StagingConfig,
    prod=ProductionConfig
)

key = BaseConfig.SECRET_KEY