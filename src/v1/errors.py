from flask import jsonify
from . import v1


def process_response(status_code, data):
    """
    this function processes any request and returns the appropriate
    content type based on the mime-type set in the request header.
    """
    data.update({
        "success": False
    })
    response = jsonify(data)
    response.status_code = status_code
    return response


@v1.errorhandler(400)
def custom_error(message):
    """Returns a custom defined error message"""
    context = {
        "error": "bad request",
        "message": message,
    }
    return process_response(400, context)


@v1.app_errorhandler(500)
def internal_server_error(e):
    """
    Returns a 500 status code for an internal server error and appropriate
    error message
    """
    context = {'error': 'internal server error', 'message': e}
    return process_response(500, context)


@v1.errorhandler(400)
def validation_error(e):
    """Returns a 400 status code for data validation failure"""
    context = {'error': 'validation error', 'message': e}
    return process_response(400, context)

    