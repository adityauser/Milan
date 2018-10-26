from django.db import models




def path(instance, filename):
	return filename


class Lost(models.Model):
	Photo = models.FileField(upload_to='media')
	person_name = models.CharField(max_length=500)
	provider_email = models.EmailField(max_length=500)
	provider_name = models.CharField(max_length=500)
	provider_number = models.CharField(max_length=10)
	#person_id = models.CharField(max_length=200)
	

class Found(models.Model):
	Photo = models.FileField(upload_to='media', null=True, blank=True)
	location = models.CharField(max_length=500)
	condition = models.CharField(max_length=500)
	provider_name = models.CharField(max_length=500)
	provider_email = models.CharField(max_length=500)
	provider_number = models.CharField(max_length=10)
	#person_id = models.CharField(max_length=200)

class idlost(models.Model):
	link = models.OneToOneField(
	    Lost,
	    on_delete=models.CASCADE,
	    primary_key=True,
	)
	person_id = models.CharField(max_length=200)

class idfound(models.Model):
	link = models.OneToOneField(
	    Found,
	    on_delete=models.CASCADE,
	    primary_key=True,
	)
	person_id = models.CharField(max_length=200)




