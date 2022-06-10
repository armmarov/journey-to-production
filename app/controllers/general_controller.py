import logging


def health():
    logging.debug("health")

    response_object = {
        "status": "Success",
        "message": "Service is healthy",
    }

    return response_object, 200