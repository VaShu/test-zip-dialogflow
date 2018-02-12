from flask import request
from flask import make_response
from manage import app
from .. import main
import json


@main.route('/webhook', methods=['GET', 'POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    question = req.get('queryResult').get('queryText')
    answer = req.get('queryResult').get('fulfillmentText')

    app.logger.info("from bot - Next dialog:")
    app.logger.info(f'question => : {question}')
    app.logger.info(f'answer => : {answer}')

    res = {
        'speech': 'Complete',
        'displayText': 'Complete',
        'source': 'Myself'
    }
    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r
