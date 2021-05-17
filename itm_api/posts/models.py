from django.db import models

class Image(models.Model):
	fileurl = models.CharField(max_length=100)
	datetime = models.CharField(max_length=20)
	location = models.CharField(max_length=100)
	uploaded_by = models.CharField(max_length=50)
	tags = models.CharField(max_length=500)
	thumbnail = models.CharField(max_length=100)

	def __str__(self):
		return self.fileurl

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    year_published = models.CharField(max_length=10)
    review = models.PositiveIntegerField()

    def __str__(self):
        return self.title
