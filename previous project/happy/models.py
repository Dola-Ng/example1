from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Comment(models.Model):
	comment = models.TextField()


	def __str__(self):
		return self.comment
# Create your models here.
