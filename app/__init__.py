from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

# app.config.from_object(config_by_name['dev'])

from app.routes.general_route import general_api

app.register_blueprint(general_api, url_prefix='/')