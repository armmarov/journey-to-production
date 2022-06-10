from http import HTTPStatus
from flask import Blueprint, request, jsonify
from flasgger import swag_from

from app.controllers.general_controller import health

general_api = Blueprint('general_api', __name__)


@general_api.route('/health', methods=(['GET']))
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            "status": "Success",
            "message": "Service is healthy",
        }
    }
})
def health_route():
    """
    Routing for health controller
    """
    return health()