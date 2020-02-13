from service import application

if __name__ == '__main__':
    application.config['DEBUG'] = True
    application.config['PROPAGATE_EXCEPTION'] = True
    application.run(debug=True, host='localhost', port=5001)