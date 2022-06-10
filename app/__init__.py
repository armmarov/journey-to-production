import os
import logging

from flask import Flask
from flasgger import Swagger
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

def create_app():
  
  app = Flask(__name__)
  swagger = Swagger(app)
  CORS(app)

  app.config.from_object('app.config')

  db = SQLAlchemy(app)
  migrate = Migrate(app, db)

  # Logger settings
  logging.basicConfig(level=logging.DEBUG,
                      format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                      datefmt='%Y-%m-%d %H:%M:%S',
                      handlers=[logging.StreamHandler()])
  logger = logging.getLogger()

  register_blueprints(app)

  return app, db

def register_blueprints(app):

  from app.routes.general_route import general_api

  app.register_blueprint(general_api, url_prefix='/')

app, db = create_app()