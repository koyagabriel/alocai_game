from typing import Any
from src.v1.errors import validation_error, internal_server_error, custom_error

class BaseException_(BaseException):
    def __init__(self, error_message: Any, propagate: bool=False) -> None:
        self.error: Any = error_message
        self.propagate: bool = propagate

    @property
    def should_propagate(self) -> bool:
        return self.propagate


class ValidationException(BaseException_):

    def broadcast(self):
        return validation_error(self.error)


class ServerException(BaseException_):

    def broadcast(self):
        return internal_server_error(self.error)


class CustomException(BaseException_):
    def broadcast(self):
        return custom_error(self.error)
    


class SwaggerException:
    
    @staticmethod
    def handler(error, data, schema):
        error_message: str = error.message
        if len(error.path):
            error_message = f"{error.path[0]}: ({error.message})"
        raise ValidationException(error_message, propagate=True)
