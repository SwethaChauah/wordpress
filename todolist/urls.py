from django.conf.urls import patterns, url

from friends import views

urlpatterns = patterns('',
    url(r'^$', views.first, name='first'),
    url(r'^$', views.second, name='second'),
    url(r'^$', views.login, name='login')
)
