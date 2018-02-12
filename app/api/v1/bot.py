from flask import jsonify
from . import api


@api.route('/bot/<string:text_quest>')
def get_answer(text_quest):
    if text_quest is not None:
        msg = {"question": text_quest}
        print("from bot - qw:", text_quest)
        return jsonify(msg)
    else:
        msg = {"msg": "not question - not answer"}
        return jsonify(msg)
