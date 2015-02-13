from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout

@csrf_exempt
def vlab(request,page):
	if page=="sample":
		return render_to_response('vlabdemo/sample.html')
	if page=="textbox":
		return render_to_response('vlabdemo/textbox.html')
	if page=="home":
		if not hasattr(request.user, 'email'):
			return redirect('http://127.0.0.1:8000')
		user_email = request.user.email
		user_name = request.user.username
		user = User.objects.filter(username=user_name, email=user_email)
		template = loader.get_template('vlabdemo/vlabhome.html')
		context = RequestContext(request,{'request': request,})
		return HttpResponse(template.render(context))
		#return render_to_response('vlabdemo/vlabhome.html', context)
	if page=="mainloginpage":
		if not hasattr(request.user, 'email'):
			return redirect('http://127.0.0.1:8000')
		return render_to_response('vlabdemo/mainloginpage.html')
	if page=="logout":
		#user_email = request.user.email
		#print user_email
		auth_logout(request)
		return render_to_response('vlabdemo/mainloginpage.html', {}, RequestContext(request))
		