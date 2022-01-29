from functools import wraps
from marshmallow import ValidationError

from src.v1.errors import custom_error, validation_error
from src.v1.exceptions import ValidationException, CustomException


def catch_exceptions(default_error_message):
    def wrap(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except CustomException as e:
                if e.should_propagate:
                    return e.broadcast()
                return custom_error(default_error_message)
            except ValidationException as e:
                if e.should_propagate:
                    return e.broadcast()
                return validation_error(default_error_message)
            except ValidationError as e:
                return validation_error(e.messages)
            except BaseException as e:
                return custom_error(default_error_message)
        return decorated_function
    return wrap
