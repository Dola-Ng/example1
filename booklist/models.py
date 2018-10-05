from django.db import models
from django.conf import settings

class TextMessage(models.Model):
	book = models.CharField (max_length=20, blank= False)
	review = models.CharField (max_length=50, blank= True)

	def __str__(self):
		return self.book + " " + self.message 