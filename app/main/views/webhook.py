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

# from dialogflow import *
# import action_methods
#
# def processRequest(req):
#     if req["status"]["code"] == 200:
#         reply_message = response["result"]["fulfillment"]["speech"]
#         try:
#             intent,action,entitiy = get_intent_action_entity(response)
#         except KeyError:
#             pass
#         print intent,entitiy,action
#         if action:
#             try:
#                 methodToCall = getattr(action_methods,action)
#                 outcome = methodToCall(entitiy)
#                 reply_message = format_message(action,reply_message,outcome)
#             except AttributeError:
#                 pass
#     return {"speech": reply_message,
#             "displayText": reply_message,
#             # "data": data,
#             "contextOut": [entity],
#             "source": "webbot-api"
#             }
#
# @app.route('/webhook',methods = ["POST"])
# def webhook():
#     req = request.get_json(silent=True, force=True)
#     print("Request:")
#     print(json.dumps(req, indent=4))
#     res = processRequest(req)
#     res = json.dumps(res, indent=4)
#     r = make_response(res)
#     print res
#     r.headers['Content-Type'] = 'application/json'
#     return r

#
# #!/usr/bin/env python
# import json
# import os
#
# from flask import Flask
# from flask import request
# from flask import make_response
#
# # Flask app should start in global layout
# app = Flask(__name__)
#
#
# @app.route('/webhook', methods=['POST'])
# def webhook():
#     req = request.get_json(silent=True, force=True)
#
#     print("Request:")
#     print(json.dumps(req, indent=4))
#
#     res = makeWebhookResult(req)
#
#     res = json.dumps(res, indent=4)
#     print(res)
#     r = make_response(res)
#     r.headers['Content-Type'] = 'application/json'
#     return r
#
# def makeWebhookResult(req):
#     if req.get("result").get("action") != "shipping.cost":
#         return {}
#     result = req.get("result")
#     parameters = result.get("parameters")
#     zone = parameters.get("bank-name")
#
#     cost = {'Andhra Bank':'6.85%', 'Allahabad Bank':'6.75%', 'Axis Bank':'6.5%', 'Bandhan bank':'7.15%', 'Bank of Maharashtra':'6.50%', 'Bank of Baroda':'6.90%', 'Bank of India':'6.60%', 'Bharatiya Mahila Bank':'7.00%', 'Canara Bank':'6.50%', 'Central Bank of India':'6.60%', 'City Union Bank':'7.10%', 'Corporation Bank':'6.75%', 'Citi Bank':'5.25%', 'DBS Bank':'6.30%', 'Dena Bank':'6.80%', 'Deutsche Bank':'6.00%', 'Dhanalakshmi Bank':'6.60%', 'DHFL Bank':'7.75%', 'Federal Bank':'6.70%', 'HDFC Bank':'5.75% to 6.75%', 'Post Office':'7.10%', 'Indian Overseas Bank':'6.75%', 'ICICI Bank':'6.25% to 6.9%', 'IDBI Bank':'6.65%', 'Indian Bank':'4.75%', 'Indusind Bank':'6.85%', 'J&K Bank':'6.75%', 'Karnataka Bank':'6.50 to 6.90%', 'Karur Vysya Bank':'6.75%', 'Kotak Mahindra Bank':'6.6%', 'Lakshmi Vilas Bank':'7.00%', 'Nainital Bank':'7.90%', 'Oriental Bank of Commerce':'6.85%', 'Punjab National Bank':'6.75%', 'Punjab and Sind Bank':'6.4% to 6.80%', 'Saraswat bank':'6.8%', 'South Indian Bank':'6% to 6.75%', 'State Bank of India':'6.75%', 'Syndicate Bank':'6.50%', 'Tamilnad Mercantile Bank Ltd':'6.90%', 'UCO bank':'6.75%', 'United Bank Of India':'6%', 'Vijaya Bank':'6.50%', 'Yes Bank':'7.10%'}
#
#     speech = "The interest rate of " + zone + " is " + str(cost[zone])
#     print("Response:")
#     print(speech)
#     return {
#         "speech": speech,
#         "displayText": speech,
#         #"data": {},
#         #"contextOut": [],
#         "source": "BankRates"
#     }

