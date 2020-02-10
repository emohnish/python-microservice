from flask import Flask

application = Flask(__name__)

@application.route('/')
def hello():
    return "Hello World"


@application.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)