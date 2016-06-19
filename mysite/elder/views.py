from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import Family
from .line import bot_send_message

# Create your views here.
def index(request):

    if request.method == 'POST':
        form = GestureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            elder = form.cleaned_data['elder']
            msg = form.cleaned_data['video']
            ask_family(elder, msg)
            return HttpResponse('thanks')
    else:
        form = GestureForm()
    return render(request, 'name.html', {'form': form})


def ask_family(name, msg):
    # query family member
    members = Family.objects.filter(elder=name)
    for member in members:
        print member.name
        send_mail(member.line, msg)
    

def send_mail(line_mid, msg):
    bot_send_message(line_mid, msg)
    

def file_test(request):
    if request.method == 'POST':
        form = TestForm(request.POST, request.FILES)
        print request.POST
        print request.body
        if form.is_valid():
            bot_send_message(msg="valid")
            return HttpResponse('thanks')
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


