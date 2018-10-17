from django.db import models
from gdstorage.storage import GoogleDriveStorage, GoogleDrivePermissionType, GoogleDrivePermissionRole, GoogleDriveFilePermission

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()



def path(instance, filename):
	return filename


class Lost(models.Model):
	Photo = models.ImageField()
	person_name = models.CharField(max_length=500)
	provider_email = models.EmailField(max_length=500)
	provider_name = models.CharField(max_length=500)

class Found(models.Model):
	Photo = models.ImageField()
	location = models.CharField(max_length=500)
	condition = models.CharField(max_length=500)
	provider_name = models.CharField(max_length=500)
	provider_email = models.CharField(max_length=500)