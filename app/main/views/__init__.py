from flask import current_app as app, send_from_directory
import os


from .index import *
from .bot import *
from .zip import *


@main.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
