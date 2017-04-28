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
        Callpost('keypress/Lit_%20')
      else:
        Callpost('keypress/Lit_{}'.format(x))


@ask.launch
def launch():
    speech_text = 'Welcome to the Alexa Skills Kit'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)

@ask.intent('Home')
def Roku_Home():
    speech_text = 'Going Home'
    Callpost('keypress/home')
    return statement(speech_text).simple_card('RokuHome', speech_text)
    
@ask.intent('Searchroku')
def SearchPlex(Text):
    speech_text = "Searching for {}".format(Text)
    Callpost('keypress/home')
    Callpost('keypress/home')
    sleep(0.2200)
    Callpost('keypress/down')
    sleep(0.150)
    Callpost('keypress/down')
    sleep(0.150)
    Callpost('keypress/down')
    sleep(0.150)
    Callpost('keypress/down')
    sleep(0.150)
    Callpost('keypress/down')
    sleep(0.150)
    Callpost('keypress/select')
    sleep(0.800)
    createTypeSequence(Text)
    sleep(0.150)
    Callpost('keypress/right')
    sleep(0.150)
    Callpost('keypress/right')
    sleep(0.150)
    Callpost('keypress/right')
    sleep(0.150)
    Callpost('keypress/right')
    sleep(0.150)
    Callpost('keypress/right')
    sleep(0.150)
    Callpost('keypress/right')
    sleep(0.500)
    Callpost('keypress/select')
    sleep(1.700)
    Callpost('keypress/select')
    sleep(4.0)
    return statement(speech_text).simple_card("Searchroku", speech_text)

@ask.intent('SearchPlex')
def SearchPlex(Text):
    speech_text = "Searching for {}".format(Text)
    Callpost('keypress/home')
    Callpost('keypress/home')
    sleep(0.2200)
    Callpost('launch/13535')
    sleep(7.250)
    Callpost('keypress/up')
    sleep(0.250)
    Callpost('keypress/select')
    sleep(0.800)
    createTypeSequence(Text)
    sleep(0.150)
    Callpost('keypress/right')
    sleep(0.150)
    Callpost('keypress/right')
    sleep(0.150)
    Callpost('keypress/right')
    sleep(0.150)
    Callpost('keypress/right')
    sleep(0.150)
    Callpost('keypress/right')
    sleep(0.150)
    Callpost('keypress/right')
    sleep(0.500)
    Callpost('keypress/select')
    sleep(1.700)
    Callpost('keypress/select')
    sleep(4.0)
    return statement(speech_text).simple_card("Searchplex", speech_text)

@ask.session_ended
def session_ended():
    return "{}", 200




if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)
