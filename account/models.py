from django.db import models
from django.contrib import admin

# Create your models here.
class Users(models.Model):
	username = models.CharField(max_length=50)
	passwd = models.CharField(max_length=50)
	email = models.EmailField()
	
	def __unicode__(self):
		return self.username
		
class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'email')
admin.site.register(Users, UserAdmin)
