from django.db import models
from django.conf import settings

class Booklist(models.Model):
	book = models.CharField (max_length=20)
	review = models.CharField (max_length=50)
	date = models.DateTimeField(auto_now_add=True)

	
def __str__(self):
	return self.book
