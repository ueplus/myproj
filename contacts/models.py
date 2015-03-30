from django.db import models
from django.contrib import admin

# Create your models here.
class contacts(models.Model):
	name = models.CharField(max_length=20)
	tel = models.CharField(max_length=16)
	birth = models.DateField()
	def __unicode__(self):
		return self.name
		
class UserAdmin(admin.ModelAdmin):
	list_display = ('name', 'tel', 'birth')
admin.site.register(contacts, UserAdmin)		