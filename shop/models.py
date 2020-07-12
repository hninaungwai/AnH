from django.db import models

# Create your models here.
class Pharmacy(models.Model):
	name = models.CharField(max_length=255)
	batch = models.IntegerField()
	price = models.CharField(max_length=225)
	promotion = models.CharField(max_length=255)
	foc = models.CharField(max_length=255)
	exp = models.DateTimeField()
	start = models.DateTimeField('date published')

	def __str__(self):
		return self.name