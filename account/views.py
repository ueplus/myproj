#coding=utf-8
import datetime
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from account.models import Users

class RegUserForm(forms.Form):
	username = forms.CharField(label='姓名',max_length=10)
	password = forms.CharField(label='密码',widget=forms.PasswordInput())
	email= forms.CharField(label='邮箱',)
    
class LoginUserForm(forms.Form):
	username = forms.CharField(label='姓名',max_length=10)
	password = forms.CharField(label='密码',widget=forms.PasswordInput())
	

def register(req):
	if req.method == 'POST':
		uf = RegUserForm(req.POST)
		if uf.is_valid():
			username = uf.cleaned_data['username']
			password = uf.cleaned_data['password']
			email = uf.cleaned_data['email']
			
			user = Users.objects.filter(username=username)
			if user:
				return render_to_response( 'account/warning.html',{'message':"该账号已被注册过，请重新物色一个"})
				
			Users.objects.create(username= username,passwd=password,email=email)
			return render_to_response( 'account/warning.html',{'message':"恭喜您，注册成功！"})
	else:
		uf = RegUserForm()
	return render_to_response( 'account/register.html',{'uf':uf, 'date':datetime.date.today()}, context_instance=RequestContext(req))
    

def login(req):
	if req.method == 'POST':
		uf = LoginUserForm(req.POST)
		if uf.is_valid():
			username = uf.cleaned_data['username']
			passwd = uf.cleaned_data['password']
			user = Users.objects.filter(username=username, passwd=passwd)

			if user:
				response = HttpResponseRedirect('/account/index/')
				response.set_cookie('username',username,3600)
				return response
		else:
			return HttpResponseRedirect('/account/login')
	else:
		pass
	return render_to_response('account/login.html',{'date':datetime.date.today()})
	

def index(req):
	username = req.COOKIES.get('username')
	if username == None:
		return HttpResponseRedirect('/account/login',{'date':datetime.date.today()})
		
	return render_to_response('account/index.html',{'date':datetime.date.today(),'username':username})

def logout(req):
	response = HttpResponse('logout!')
	response.delete_cookie('username')
	return response