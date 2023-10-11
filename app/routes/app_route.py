from http import HTTPStatus
from flask import Blueprint, render_template

from app.controllers.yolo_controller import predict_image

app_ui = Blueprint('app_ui', __name__)


@app_ui.route('/', methods=(['GET']))
def index():
    return render_template('index.html')