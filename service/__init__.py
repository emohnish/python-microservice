from flask import Flask, render_template
from error_handling.bindings import bind_error_handlers
from service.exception.exceptions import ForbiddenRouteError


application = Flask(__name__)

REGISTERED_EXC = {
    #400: ['AgeFormatError', 'UnderAgeError'],
    403: [ForbiddenRouteError],
    #404: ['ResourceNotFound'],
}

bind_error_handlers(application, register_status_dict=REGISTERED_EXC)


@application.route('/')
def hello():
    return render_template('hello.html'), 200


@application.route('/<name>')
def hello_name(name):
    if(name=='mohnish'):
       raise ForbiddenRouteError()
    
    return "Hello {}!".format(name)