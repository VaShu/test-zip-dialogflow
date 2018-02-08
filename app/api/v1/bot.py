from flask import jsonify
from . import api
from manage import app
import dialogflow

# dialogflow.ai account info
CLIENT_ACCESS_TOKEN = "40371e6bed654b3daa71e2c6de958326"
# ai = dialogflow.AgentsClient()

@api.route('/*bo t/<string:text_quest>')
def get_answer(text_quest):
    if text_quest is not None:
        msg = {"question": text_quest}
        print("from bot - qw:", text_quest)
        app.logger.info("from bot - qw:")
        app.logger.info(text_quest)
        return jsonify(msg)
    else:
        msg = {"msg": "not question - not answer"}
        return jsonify(msg)
