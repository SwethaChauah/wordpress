from django.forms import ModelForm
from friends.models import Friends1

class Addfriendform(ModelForm):
    class Meta:
        model = Friends1
        fields = ['name1']

