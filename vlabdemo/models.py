from django.db import models
from django import forms
from django.contrib.auth.models import User
	
class vlabloginmodel(models.Model):
	temp = models.ForeignKey(User)
	name = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	def __unicode__(self):
		return self.name1 