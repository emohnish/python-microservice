#Register Flask Error Handlers.
from error_handling.exceptions import (
    InvalidServerErrorsList,
    UnsupportedHTTPStatus
)

from error_handling.handlers import (
    handle_error_page_400,
    handle_error_page_401,
    handle_error_page_402,
    handle_error_page_403,
    handle_error_page_404,
    handle_error_page_405,
    handle_error_page_406,
    handle_error_page_407,
    handle_error_page_408,
    handle_error_page_409,
    handle_error_page_410,
    handle_error_page_411,
    handle_error_page_412,
    handle_error_page_413,
    handle_error_page_414,
    handle_error_page_415,
    handle_error_page_416,
    handle_error_page_417,
    handle_error_page_500,
    handle_error_page_501,
    handle_error_page_502,
    handle_error_page_503,
    handle_error_page_504,
    handle_error_page_505
)

HTTP_STATUS_TO_HANDLER = {
    400: handle_error_page_400,  # Bad Request
    401: handle_error_page_401,  # Unauthorized
    402: handle_error_page_402,  # Payment Required
    403: handle_error_page_403,  # Forbidden
    404: handle_error_page_404,  # Not Found
    405: handle_error_page_405,  # Method Not Allowed
    406: handle_error_page_406,  # Not Acceptable
    407: handle_error_page_407,  # Proxy Authentication Required
    408: handle_error_page_408,  # Request Timeout
    409: handle_error_page_409,  # Conflict
    410: handle_error_page_410,  # Gone
    411: handle_error_page_411,  # Length Required
    412: handle_error_page_412,  # Precondition Failed
    413: handle_error_page_413,  # Request Entity Too Large
    414: handle_error_page_414,  # Request-URI Too Long
    415: handle_error_page_415,  # Unsupported Media Type
    416: handle_error_page_416,  # Requested Range Not Satisfiable
    417: handle_error_page_417,  # Expectation Failed
    500: handle_error_page_500,  # Internal Server Error
    501: handle_error_page_501,  # Not Implemented
    502: handle_error_page_502,  # Bad Gateway
    503: handle_error_page_503,  # Service Unavailable
    504: handle_error_page_504,  # Gateway Timeout
    505: handle_error_page_505,  # HTTP Version Not Supported
}

REGISTERED_EXCEPTIONS = {
    400: [],
    401: [],
    402: [],
    403: [],
    404: [], 
    405: [],
    406: [],
    407: [],
    408: [],
    409: [],
    410: [],
    411: [],
    412: [],
    413: [],
    414: [],
    415: [],
    416: [],
    417: [],
    500: [],
    501: [],
    502: [],
    503: [],
    504: [],
    505: [],
}


def register_exceptions(status_code, exceptions):

    if status_code not in HTTP_STATUS_TO_HANDLER:
        raise UnsupportedHTTPStatus(status_code)

    invalid_objects = [v for v in exceptions if not issubclass(v, Exception)]
    if invalid_objects:
        raise InvalidServerErrorsList(invalid_objects)

    REGISTERED_EXCEPTIONS[status_code].extend(exceptions)


def bind_error_handlers(app, register_status_dict={}):

    if register_status_dict:
        for status_code, exc_type_list in register_status_dict.items():
            register_exceptions(status_code, exc_type_list)

    for status_code, exc_type_list in REGISTERED_EXCEPTIONS.items():
        for exec_type in exc_type_list:
            app.register_error_handler(
                exec_type, HTTP_STATUS_TO_HANDLER.get(status_code, handle_error_page_500))
