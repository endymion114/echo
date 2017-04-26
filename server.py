import logging
import os
import requests
import time

from flask import Flask
from flask_ask import Ask, request, session, question, statement
from time import sleep


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)


@ask.launch
def launch():
    speech_text = 'Welcome to the Alexa Skills Kit'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)

@ask.intent('Home')
def Roku_Home():
    speech_text = 'Home Menu'
    url     = 'http://10.0.0.155:8060/keypress/home'
    payload = {}
    headers = {}
    res = requests.post(url, data=payload, headers=headers)
    return statement(speech_text).simple_card('RokuHome', speech_text)

@ask.intent('Up')
def Roku_Up():
    speech_text = ''
    url     = 'http://10.0.0.155:8060/keypress/Up'
    payload = {}
    headers = {}
    res = requests.post(url, data=payload, headers=headers)
    return statement(speech_text).simple_card('RokuUp', speech_text)

@ask.intent('Uptwo')
def Roku_Uptwo():
    speech_text = ''
    url     = 'http://10.0.0.155:8060/keypress/Up'
    payload = {}
    headers = {}
    res = requests.post(url, data=payload, headers=headers)
    sleep(0.5)
    res = requests.post(url, data=payload, headers=headers)
    return statement(speech_text).simple_card('RokuUptwo', speech_text)

@ask.session_ended
def session_ended():
    return "{}", 200


if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)
