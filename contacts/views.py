from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from contacts.models import contacts

def display(request):
	user=0
	try:
		contact=contacts.objects.get(name = 'wuxiong')
		contactlist=contacts.objects.all()
	except contacts.DoesNotExist:
		raise Http404

	return render_to_response("contacts.html",{"user":user,"contactlist":contactlist})
