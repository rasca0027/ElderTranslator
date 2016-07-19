# coding=UTF-8

from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import * 
from .line import *

# Create your views here.

def get_youtube(video_obj):
    pass

def file_test(request):
    
    if request.method == 'POST':
        
        form = TestForm(request.POST, request.FILES)
        print request.POST
        print request.FILES
        
        if form.is_valid():
            
            print 'valid'
            
            # save file and model
            elder_name = request.POST['name']
            elder_obj = Elder.objects.get(name=elder_name)
            upload_video = request.FILES['video']
            gesture = Gesture(elder=elder_obj,
                    video=upload_video)
            gesture.save()
            
            # get family 
            members = Family.objects.filter(elder=elder_obj)
            for member in members:
                print member.name
                line_mid = member.line
                # send line
                video_url, video_preview_img = get_youtube(upload_video)
                r = bot_send_video(line_mid, gesture, video_url, video_preview_img)
                print r.content
            
            return HttpResponse('thanks')
        
        else:
            print 'not valid'
    
    else:
        form = TestForm()
    return render(request, 'test.html', {'form': form})



def bot_callback(request):
    
    import json
    
    # receive msg and send to android
    data = json.loads(request.body)
    content = data['result'][0]['content']['text']
    people = data['result'][0]['content']['from']

    print content, people
    
    # to android!!

    return HttpResponse(status=200)


def bot_test_view(request):

    r = bot_send_message(msg='test success')
    print r.content
    return HttpResponse('bot test')



