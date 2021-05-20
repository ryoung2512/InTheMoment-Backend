from django.db import models

class Image(models.Model):
	fileurl = models.CharField(max_length=300)
	title = models.CharField(max_length=100)
	datetime = models.CharField(max_length=20)
	location = models.CharField(max_length=100)
	author = models.CharField(max_length=50)
	tags = models.CharField(max_length=500)
	thumbnail = models.CharField(max_length=100)
	video = models.BooleanField()

	def __str__(self):
		return self.fileurl