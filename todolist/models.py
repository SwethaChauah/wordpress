from django.db import models
from django import forms
from django.contrib.auth.models import User
	
class Friends1(models.Model):
	temp1 = models.ForeignKey(User)
	name1 = models.CharField(max_length=200)
	location1 = models.CharField(max_length=200)
	def __unicode__(self):
		return self.name1  

