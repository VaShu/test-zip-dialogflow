from flask import request
from flask import make_response
from .. import main
import json
import os
import urllib


@main.route('/webhook', methods=['GET', 'POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    # res = makeWebhookResult(req)

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


#
# def makeWebhookResult(req):
#     result = req.get('result')
#     parameters = result.get('parameters')
#     zone = parameters.get('xx.test1')
#     leson = parameters.get('xx.test2')
#
#     speech = zone + leson
#     print('Response:')
#     print(speech)
#     return {
#         'speech': speech,
#         'displayText': speech,
#         ##"data": {},
#         ##"contextOut": [],
#         'source': 'leson'
#     }

"""
The issue is that the JSON object returned by the script is always empty. Using ngrok, 
I got something like this in the fulfillment key of the object:

"fulfillment": {
        "speech": "",
        "messages": []
    }
 https://stackoverflow.com/questions/47929433/issue-with-building-a-webhook-for-dialogflow   
"""