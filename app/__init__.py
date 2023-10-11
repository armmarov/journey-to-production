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

  from app.routes.app_route import app_ui
  from app.routes.rec_engine_route import rec_engine_api
  from app.routes.yolo_route import yolo_api

  app.register_blueprint(app_ui, url_prefix='/')
  app.register_blueprint(rec_engine_api, url_prefix='/rec')
  app.register_blueprint(yolo_api, url_prefix='/yolo')

app, db = create_app()