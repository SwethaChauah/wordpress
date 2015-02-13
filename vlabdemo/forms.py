from django.forms import ModelForm
from vlabdemo.models import vlabloginmodel

class Adduserform(ModelForm):
    class Meta:
        model = vlabloginmodel
        fields = ['name']