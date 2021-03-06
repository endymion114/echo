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


@ask.intent('Uptwo')
def Uptwo():
    speech_text = 'moving Up two'
    Callpost('keypress/Up')
    sleep(0.150)
    Callpost('keypress/Up')
    sleep(0.150)
    return statement(speech_text).simple_card('Uptwo', speech_text)

@ask.intent('Upthree')
def Upthree():
    speech_text = 'moving Up three'
    Callpost('keypress/Up')
    sleep(0.150)
    Callpost('keypress/Up')
    sleep(0.150)
    Callpost('keypress/Up')
    sleep(0.150)
    return statement(speech_text).simple_card('Upthree', speech_text)

@ask.intent('Upfour')
def Upfour():
    speech_text = 'moving Up four'
    Callpost('keypress/Up')
    sleep(0.150)
    Callpost('keypress/Up')
    sleep(0.150)
    Callpost('keypress/Up')
    sleep(0.150)
    Callpost('keypress/Up')
    sleep(0.150)
    return statement(speech_text).simple_card('Upfour', speech_text)

@ask.intent('Upfive')
def Upfive():
    speech_text = 'moving Up five'
    Callpost('keypress/Up')
    sleep(0.150)
    Callpost('keypress/Up')
    sleep(0.150)
    Callpost('keypress/Up')
    sleep(0.150)
    Callpost('keypress/Up')
    sleep(0.150)
    Callpost('keypress/Up')
    sleep(0.150)
    return statement(speech_text).simple_card('Upfive', speech_text)

@ask.intent('Downtwo')
def Downtwo():
    speech_text = 'moving Down two'
    Callpost('keypress/Down')
    sleep(0.150)
    Callpost('keypress/Down')
    sleep(0.150)
    return statement(speech_text).simple_card('Downtwo', speech_text)

@ask.intent('Downthree')
def Downthree():
    speech_text = 'moving Down three'
    Callpost('keypress/Down')
    sleep(0.150)
    Callpost('keypress/Down')
    sleep(0.150)
    Callpost('keypress/Down')
    sleep(0.150)
    return statement(speech_text).simple_card('Downthree', speech_text)

@ask.intent('Downfour')
def Downfour():
    speech_text = 'moving Down four'
    Callpost('keypress/Down')
    sleep(0.150)
    Callpost('keypress/Down')
    sleep(0.150)
    Callpost('keypress/Down')
    sleep(0.150)
    Callpost('keypress/Down')
    sleep(0.150)
    return statement(speech_text).simple_card('Downfour', speech_text)

@ask.intent('Downfive')
def Downfive():
    speech_text = 'moving Down five'
    Callpost('keypress/Down')
    sleep(0.150)
    Callpost('keypress/Down')
    sleep(0.150)
    Callpost('keypress/Down')
    sleep(0.150)
    Callpost('keypress/Down')
    sleep(0.150)
    Callpost('keypress/Down')
    sleep(0.150)
    return statement(speech_text).simple_card('Downfive', speech_text)

@ask.intent('Righttwo')
def Righttwo():
    speech_text = 'moving Right two'
    Callpost('keypress/Right')
    sleep(0.150)
    Callpost('keypress/Right')
    sleep(0.150)
    return statement(speech_text).simple_card('Righttwo', speech_text)

@ask.intent('Rightthree')
def Rightthree():
    speech_text = 'moving Right three'
    Callpost('keypress/Right')
    sleep(0.150)
    Callpost('keypress/Right')
    sleep(0.150)
    Callpost('keypress/Right')
    sleep(0.150)
    return statement(speech_text).simple_card('Rightthree', speech_text)

@ask.intent('Rightfour')
def Rightfour():
    speech_text = 'moving Right four'
    Callpost('keypress/Right')
    sleep(0.150)
    Callpost('keypress/Right')
    sleep(0.150)
    Callpost('keypress/Right')
    sleep(0.150)
    Callpost('keypress/Right')
    sleep(0.150)
    return statement(speech_text).simple_card('Rightfour', speech_text)

@ask.intent('Rightfive')
def Rightfive():
    speech_text = 'moving Right five'
    Callpost('keypress/Right')
    sleep(0.150)
    Callpost('keypress/Right')
    sleep(0.150)
    Callpost('keypress/Right')
    sleep(0.150)
    Callpost('keypress/Right')
    sleep(0.150)
    Callpost('keypress/Right')
    sleep(0.150)
    return statement(speech_text).simple_card('Rightfive', speech_text)

@ask.intent('Lefttwo')
def lefttwo():
    speech_text = 'moving left two'
    Callpost('keypress/left')
    sleep(0.150)
    Callpost('keypress/left')
    sleep(0.150)
    return statement(speech_text).simple_card('lefttwo', speech_text)

@ask.intent('Leftthree')
def leftthree():
    speech_text = 'moving left three'
    Callpost('keypress/left')
    sleep(0.150)
    Callpost('keypress/left')
    sleep(0.150)
    Callpost('keypress/left')
    sleep(0.150)
    return statement(speech_text).simple_card('leftthree', speech_text)

@ask.intent('Leftfour')
def leftfour():
    speech_text = 'moving left four'
    Callpost('keypress/left')
    sleep(0.150)
    Callpost('keypress/left')
    sleep(0.150)
    Callpost('keypress/left')
    sleep(0.150)
    Callpost('keypress/left')
    sleep(0.150)
    return statement(speech_text).simple_card('leftfour', speech_text)

@ask.intent('Leftfive')
def leftfive():
    speech_text = 'moving left five'
    Callpost('keypress/left')
    sleep(0.150)
    Callpost('keypress/left')
    sleep(0.150)
    Callpost('keypress/left')
    sleep(0.150)
    Callpost('keypress/left')
    sleep(0.150)
    Callpost('keypress/left')
    sleep(0.150)
    return statement(speech_text).simple_card('leftfive', speech_text)

@ask.intent('Captionon')
def captionon():
    speech_text = 'Caption on'
    Callpost('keypress/info')
    sleep(0.150)
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
    Callpost('keypress/right')
    sleep(0.150)
    Callpost('keypress/info')
    sleep(0.150)
    return statement(speech_text).simple_card('captionon', speech_text)

@ask.intent('Captionoff')
def captionoff():
    speech_text = 'Caption off'
    Callpost('keypress/info')
    sleep(0.150)
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
    Callpost('keypress/left')
    sleep(0.150)
    Callpost('keypress/info')
    sleep(0.150)
    return statement(speech_text).simple_card('captionoff', speech_text)

@ask.intent('Type')
def Typing(Text):
    speech_text = "Typing {}".format(Text)
    createTypeSequence(text)
    return statement(speech_text).simple_card('Type', speech_text)

@ask.intent('Search')
def Search(Text):
    speech_text = "Searching for {}".format(Text)
    createTypeSequence(text)
    return statement(speech_text).simple_card('Search', speech_text)
    
@ask.intent('SearchRoku')
def SearchRoku(Text):
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
    return statement(speech_text).simple_card("Searchplex", speech_text)

@ask.intent('Playlastyoutube')
def Last_Your_Tube():
    speech_text = 'Playing last You Tube Video'
    Callpost('keypress/home')
    sleep(0.500)
    Callpost('keypress/launch/837')
    sleep(20.000)
    Callpost('keypress/up')
    sleep(0.400)
    Callpost('keypress/up')
    sleep(0.400)
    Callpost('keypress/select')
    sleep(0.800)
    Callpost('keypress/up')
    sleep(0.800)
    Callpost('keypress/select')
    sleep(3.200)
    Callpost('keypress/select')
    sleep(3.200)
    Callpost('keypress/select')
    return statement(speech_text).simple_card('Playlastyoutube ', speech_text)

@ask.intent('PlayPause')
def play_pause():
    speech_text = 'Ok'
    Callpost('keypress/Play')
    return statement(speech_text).simple_card('play_pause', speech_text)

@ask.intent('Power')
def Power():
    speech_text = 'Ok'
    Callpost('keypress/Power')
    return statement(speech_text).simple_card('power', speech_text)

@ask.intent('Fastforward')
def Fwd():
    speech_text = 'Ok'
    Callpost('keypress/fwd')
    return statement(speech_text).simple_card('fwd', speech_text)

@ask.intent('Rewind')
def Rev():
    speech_text = 'Ok'
    Callpost('keypress/rev')
    return statement(speech_text).simple_card('rev', speech_text)

@ask.intent('Up')
def up():
    speech_text = 'Ok'
    Callpost('keypress/up')
    return statement(speech_text).simple_card('up', speech_text)

@ask.intent('Down')
def Down():
    speech_text = 'Ok'
    Callpost('keypress/down')
    return statement(speech_text).simple_card('down', speech_text)

@ask.intent('Back')
def Back():
    speech_text = 'Ok'
    Callpost('keypress/back')
    return statement(speech_text).simple_card('back', speech_text)

@ask.intent('Left')
def Left():
    speech_text = 'Ok'
    Callpost('keypress/left')
    return statement(speech_text).simple_card('left', speech_text)

@ask.intent('Instantreplay')
def Instantreplay():
    speech_text = 'Ok'
    Callpost('keypress/instantreplay')
    return statement(speech_text).simple_card('intantreplay', speech_text)

@ask.intent('Right')
def right():
    speech_text = 'Ok'
    Callpost('keypress/right')
    return statement(speech_text).simple_card('right', speech_text)

@ask.intent('Select')
def select():
    speech_text = 'Ok'
    Callpost('keypress/select')
    return statement(speech_text).simple_card('select', speech_text)


@ask.intent('Amazon')
def Amazon():
    speech_text = 'Starting Amazon'
    Callpost('/launch/13')
    return statement(speech_text).simple_card('right', speech_text)

@ask.intent('Pandora')
def Pandora():
    speech_text = 'Starting Pandora'
    Callpost('/launch/28')
    return statement(speech_text).simple_card('Pandora', speech_text)

@ask.intent('Hulu')
def Hulu():
    speech_text = 'Starting Hulu'
    Callpost('/launch/2285')
    return statement(speech_text).simple_card('Hulu', speech_text)

@ask.intent('Plex')
def Plex():
    speech_text = 'Starting Plex'
    Callpost('/launch/13535')
    return statement(speech_text).simple_card('Plex', speech_text)
            
@ask.intent('Home')
def Roku_Home():
    speech_text = 'Going Home'
    Callpost('keypress/home')
    return statement(speech_text).simple_card('RokuHome', speech_text)

@ask.intent('TV')
def Tv():
    speech_text = 'ok'
    Callpost('launch/tvinput.dtv')
    return statement(speech_text).simple_card('Tv', speech_text)
            
@ask.intent('FourK')
def FourK():
    speech_text = 'ok'
    Callpost('launch/69091')
    return statement(speech_text).simple_card('fourk', speech_text)            

@ask.intent('HBO')
def HBO():
    speech_text = 'Starting HBO'
    Callpost('launch/8378')
    return statement(speech_text).simple_card('HBO', speech_text)             

@ask.intent('FX')
def Fx():
    speech_text = 'Starting F X'
    Callpost('launch/47389')
    return statement(speech_text).simple_card('Fx', speech_text)             
 
@ask.intent('YouTube')
def youtube():
    speech_text = 'Starting YouTube'
    Callpost('launch/837')
    return statement(speech_text).simple_card('Utube', speech_text)              

@ask.intent('Netflix')
def netflix():
    speech_text = 'Starting Netflix'
    Callpost('launch/12')
    return statement(speech_text).simple_card('netflix', speech_text)               
            
@ask.session_ended
def session_ended():
    return "{}", 200




if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)
