from django.forms import ModelForm, Form, FileField, CharField
from .models import Gesture

class GestureForm(ModelForm):
    
    class Meta:
        model = Gesture
        fields = ['name', 'elder', 'video']

class TestForm(Form):
    name = FileField()
