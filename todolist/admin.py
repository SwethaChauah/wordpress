from django.contrib import admin
from friends.models import Friends1

class FriendsAdmin(admin.ModelAdmin):
    fields = ['temp1', 'name1', 'location1']
    list_display = ('temp1', 'name1', 'location1')
admin.site.register(Friends1, FriendsAdmin)

