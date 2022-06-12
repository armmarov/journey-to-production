from http import HTTPStatus
from flask import Blueprint, request, jsonify
from flasgger import swag_from

from app.controllers.ml_controller import get_recommendation

ml_api = Blueprint('ml_api', __name__)


@ml_api.route('/recommend', methods=(['POST']))
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            "status": "Success",
            "message": "List of titles",
        }
    }
})
def get_recommendation_route():
    """
    Routing for get_recommendation controller
    """

    dat = request.get_json()

    if dat:
      return jsonify(get_recommendation(title=dat.get('title')))
    else:
      output = {"status": "Failed", "message": "No input"}
      return jsonify(output)