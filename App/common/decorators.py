from functools import wraps
from http import HTTPStatus

from App.common.exceptions import (
    UserAlreadyExistException, UserNotFoundException, ValuesNullException)
from sqlalchemy.exc import IntegrityError


def exception_manager(endpoint_function):
    @wraps(endpoint_function)
    def func_wrapper(*args, **kwargs):
        try:
            return endpoint_function(*args, **kwargs)
        except (
            IntegrityError,
        ) as e:
            message = f"Server side exception occurred. Exception type: {e.__class__}, Exception message: {e}, Exception cause: {e.__cause__}"
            return {"message": message}, HTTPStatus.INTERNAL_SERVER_ERROR
        except (
            UserAlreadyExistException,
            ValuesNullException
        ) as e:
            message = f"Client side exception occurred. Exception type: {e.__class__}, Exception message: {e}, Exception cause: {e.__cause__}"
            return {"message": message}, HTTPStatus.BAD_REQUEST
        except (
            UserNotFoundException
        ) as e:
            message = f"Client side exception occurred. Exception type: {e.__class__}, Exception message: {e}, Exception cause: {e.__cause__}"
            return {"message": message}, HTTPStatus.NOT_FOUND
        except Exception as e:
            message = f"Unknown exception occurred. Exception type: {e.__class__}, Exception message: {e}, Exception cause: {e.__cause__}"
            return {"message": message}, HTTPStatus.INTERNAL_SERVER_ERROR
    return func_wrapper
