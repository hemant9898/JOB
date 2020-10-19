from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Teacher(models.Model):
	name = models.CharField(max_length=30)
	

	def __str__(self):
		return f"{self.id}: name({self.name})"




class data(models.Model):
	user = models.ManyToManyField(User, blank=True, related_name="data")
	exp = models.IntegerField()
	loc = models.CharField(max_length=30)
	skill = models.CharField(max_length=30)
	indus = models.CharField(max_length=30)
	salary = models.IntegerField()
	cname = models.CharField(max_length=30)
	def __str__(self):
		return f"{self.id}: Company Name({self.cname})"