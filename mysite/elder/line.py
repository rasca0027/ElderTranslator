from django.conf import settings
import requests
import json


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
    req = requests.post(api, data=json.dumps(body), headers=headers)
    
    return req
