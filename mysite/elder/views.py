from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import Family

# Create your views here.
def index(request):

    if request.method == 'POST':
        form = GestureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            ask_family(form.cleaned_data['elder'])
            return HttpResponse('thanks')
    else:
        form = GestureForm()
    return render(request, 'name.html', {'form': form})


def ask_family(name):
    # query family member
    members = Family.objects.filter(elder=name)
    for member in members:
        print member.name
        send_mail(member.line)
    # send line to them

def send_mail(line):
    pass
    

def file_test(request):
    if request.method == 'POST':
        form = TestForm(request.POST, request.FILES)
        print request.POST
        if form.is_valid():
            return HttpResponse('thanks')
    else:
        form = TestForm()
    return render(request, 'test.html', {'form': form})


