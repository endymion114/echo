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

def Callpost(urldata):
    url = 'http://10.0.0.155:8060/{}'.format(urldata)
    payload = {}
    headers = {}
    res = requests.post(url, data=payload, headers=headers)

def createTypeSequence(text):
    worldlist = list(text)
    for x in worldlist:
      if ord(x) == 32:
        Callpost('http://10.0.0.155:8060/keypress/Lit_%20')
      else:
        Callpost('http://10.0.0.155:8060/keypress/Lit_{}'.format(x))


@ask.launch
def launch():
    speech_text = 'Welcome to the Alexa Skills Kit'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)

@ask.intent('SearchPlex')
def SearchPlex(Text):
    speech_text = "Searching for {}".format(Text)
    Callpost('http://10.0.0.155:8060/keypress/home')
    
    return statement(speech_text).simple_card("Searchplay", speech_text)

@ask.session_ended
def session_ended():
    return "{}", 200




if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)
