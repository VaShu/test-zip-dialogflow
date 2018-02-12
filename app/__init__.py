from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import time
import logging
from logging.handlers import TimedRotatingFileHandler

from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # for debug in PyCharm
    # app.debug = False
    # app.use_debugger = True
    # app.use_reloader = True
    app.debug = True

    bootstrap.init_app(app)
    db.init_app(app)
    init_logging(app)
    current_day = time.ctime()
    app.logger.info(f"Init logging: {current_day}")

    # import blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # api
    from app.api.v1 import api as api_v1_blueprint
    app.register_blueprint(api_v1_blueprint, url_prefix='/api/v1')

    return app

def init_logging(app):

    log_path = app.config['LOGGING_PATH']

    # The maxBytes is set to this number, in order to demonstrate the generation of multiple log files (backupCount).
    # handler = RotatingFileHandler('logs/app.log', maxBytes=10000, backupCount=3)

    """
    https://docs.python.org/3.5/library/logging.handlers.html
    You can use the when to specify the type of interval. The list of possible values is below. Note that they are not case sensitive.
    
    'S' 	    Seconds
    'M' 	    Minutes
    'H' 	    Hours
    'D'     	Days
    'W0'-'W6' 	Weekday (0=Monday)
    'midnight' 	Roll over at midnight
    """
    handler = TimedRotatingFileHandler(log_path, when='midnight', interval=1, backupCount=0)

    # getLogger('__name__') - decorators loggers to file / werkzeug loggers to stdout
    # getLogger('werkzeug') - werkzeug loggers to file / nothing to stdout
    logging.getLogger('werkzeug')
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
