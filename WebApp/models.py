
from django.db import models
	
class RegistrationModel(models.Model):
    	
	first_name = models.CharField(max_length = 200)
	last_name = models.CharField(max_length = 200)
	user_id = models.CharField(max_length = 200)
	password = models.IntegerField()
	
	
	def __str__(self):
		return self.first_name

