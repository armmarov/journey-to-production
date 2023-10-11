from http import HTTPStatus
from flask import Blueprint, request, jsonify
from flasgger import swag_from

from app.controllers.yolo_controller import predict_image

yolo_api = Blueprint('yolo_api', __name__)


@yolo_api.route('/predict', methods=(['POST']))
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            "status": "Success",
            "message": "",
        }
    }
})
def predict_image_route():
    """
    Routing for predict image controller
    """

    dat = request.get_json()

    if dat:
      return jsonify(predict_image(image=dat.get('img')))
    else:
      output = {"status": "Failed", "message": "No input"}
      return jsonify(output)