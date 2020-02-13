from flask import Flask, render_template
from error_handling.bindings import bind_error_handlers
from service.exception.exceptions import ForbiddenRouteError

from log_handling.logger import Logger
from log_handling import jsonlogger

import logging

application = Flask(__name__)

REGISTERED_EXC = {
    #400: ['AgeFormatError', 'UnderAgeError'],
    403: [ForbiddenRouteError],
    #404: ['ResourceNotFound'],
}

bind_error_handlers(application, register_status_dict=REGISTERED_EXC)


handler = logging.StreamHandler()
formatterText = logging.Formatter("%(filename)s %(lineno)s")
formatterJSON = jsonlogger.JsonFormatter()

loggerText = Logger.getLogger(handler, formatterText)
loggerJSON = Logger.getLogger(handler, formatterJSON)

@application.route('/')
def hello():
    return render_template('hello.html'), 200


@application.route('/<name>')
def hello_name(name):
    if(name=='mohnish'):
       raise ForbiddenRouteError()
    
    loggerJSON.info("HELLO")
    #loggerText.info("HELLO")

    return "Hello {}!".format(name)