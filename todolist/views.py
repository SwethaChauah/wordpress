from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from friends.models import Friends1
from friends.forms import Addfriendform
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext, loader
from django.contrib.auth.models import User

@csrf_exempt
def friend(request,page):
    if page=="addfriend":
        c = {}
        if request.method == 'POST' :
            form = Addfriendform(request.POST)
            c.update(csrf(request))
            friendname = request.POST.get("name")
            #friendlocation = request.POST["location"]
            user=request.user
            new_list_object = Friends1.objects.create(temp1=user, name1=friendname)
            value_id = new_list_object.id
            print "ID IS"
            print value_id
            context = {'value_id':value_id}
        return HttpResponse(value_id)
    if page=="update":
        fid = request.GET["fid"]
        updateFriend = Friends1.objects.get(pk=fid)
        c = {}
        if request.method == 'POST' :
            form = Addfriendform(request.POST)
            c.update(csrf(request))
            updatedfriendname = request.POST['name']
            p = Friends1.objects.get(pk=fid)
            p.name1=updatedfriendname
            p.save()
        latest_friends_list = Friends1.objects.all()
        context = {'latest_friends_list': latest_friends_list,'friends':updateFriend, 'c':c}
        return render_to_response('friends/update.html', context)
    if page=="update1":
        fid = request.POST["fid"]
        print "the value of fid is "
        print fid
        updateFriend = Friends1.objects.get(pk=fid)
        c = {}
        if request.method == 'POST' :
            print "abcd"
            form = Addfriendform(request.POST)
            c.update(csrf(request))
            updatedfriendname = request.POST["name"]
            print "friend name is" 
            print updatedfriendname
            p = Friends1.objects.get(pk=fid)
            p.name1=updatedfriendname
            print updatedfriendname
            p.save()
        latest_friends_list = Friends1.objects.all()
        context = {'latest_friends_list': latest_friends_list,'friends':updateFriend, 'c':c}
        return HttpResponse(status=200)
    if page=="delete":
        fid = request.POST["fid"]
        user = request.user
        Friends1.objects.filter(id=fid).delete()
        if request.method == 'POST':
            latest_friends_list = Friends1.objects.all()
            context = {'latest_friends_list': latest_friends_list}
        return HttpResponse(status=200)
    if page=="home":
        if not hasattr(request.user, 'email'):
            return redirect('http://127.0.0.1:8000')
        user_email = request.user.email
        user_name = request.user.username
        user = User.objects.filter(username=user_name, email=user_email)
        template = loader.get_template('friends/home.html')
        latest_friends_list = Friends1.objects.filter(temp1=user)
        context = RequestContext(request,{'request': request,
                           'latest_friends_list': latest_friends_list})
        return HttpResponse(template.render(context))
    if page=="vlablogin":
        latest_friends_list = Friends1.objects.all()
        context = {'latest_friends_list': latest_friends_list}
        return render_to_response('friends/vlablogin.html', context)
    if page=="sample":
        latest_friends_list = Friends1.objects.all()
        context = {'latest_friends_list': latest_friends_list}
        return render_to_response('friends/sample.html', context)  
