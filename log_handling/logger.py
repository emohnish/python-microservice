import logging

class Logger:

    @staticmethod
    def getLogger(handler, formatter):
        logger = logging.getLogger()
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        return logger