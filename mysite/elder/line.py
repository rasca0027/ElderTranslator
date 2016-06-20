from urllib2 import urlparse
from django.conf import settings
import requests
import json
from .models import Gesture


def bot_send_message(to_mid="u2ef38a8c1f3f1c2c63bdf9c0a629023c", msg='hi'):

    headers = {}
    headers['Content-type'] = 'application/json; charset=UTF-8'
    headers['X-Line-ChannelID'] = settings.CHANNEL_ID
    headers['X-Line-ChannelSecret'] = settings.CHANNEL_SECRET
    headers['X-Line-Trusted-User-With-ACL'] = settings.CHANNEL_MID

    api = 'https://trialbot-api.line.me/v1/events'

    body = {}
    body['to'] = [to_mid]
    body['toChannel'] = 1383378250
    body['eventType'] = "138311608800106203"

    content = {
        "contentType": 1,
        "toType": 1,
        "text": msg
    }

    body['content'] = content
    req = requests.post(api, data=json.dumps(body), headers=headers, verify=False)
    
    return req

def bot_send_video(to_mid="u2ef38a8c1f3f1c2c63bdf9c0a629023c", gesture=0):
    
    headers = {}
    headers['Content-type'] = 'application/json; charset=UTF-8'
    headers['X-Line-ChannelID'] = settings.CHANNEL_ID
    headers['X-Line-ChannelSecret'] = settings.CHANNEL_SECRET
    headers['X-Line-Trusted-User-With-ACL'] = settings.CHANNEL_MID

    api = 'https://trialbot-api.line.me/v1/events'

    body = {}
    body['to'] = [to_mid]
    body['toChannel'] = 1383378250
    body['eventType'] = "138311608800106203"

    #gesture = Gesture.objects.all()[0]
    myurl = 'https://eldertranslator.herokuapp.com/'
    video_url = urlparse.urljoin(myurl, gesture.video.url)

    content = {
        "contentType": 3,
        "toType": 1,
        "originalContentUrl": "http://127.0.0.1:8000/media/upload/sample_movie_4PeSPlq.mp4",
        "previewImageUrl": "http://www.barransclass.com/phys1090/circus/Haynes_K/penguin.jpg"
    }

    body['content'] = content
    req = requests.post(api, data=json.dumps(body), headers=headers, verify=False)
    
    return req

