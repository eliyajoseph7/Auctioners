from django.db import models
from PIL import Image

# Create your models here.
class HouseDetails(models.Model):
	n_rooms = models.IntegerField()
	TYPE = (
           ('Masters','Masters'),
           ('Non Masters','Non Masters'),
           ('I dont Know','I dont Know')
		)
	date_created = models.DateTimeField(auto_now_add=True,null=True)
	location = models.CharField(max_length=200, null=True)
	typee = models.CharField(max_length=200, null=True,choices=TYPE)
	short_disc = models.CharField(max_length=500,null=True)
	image = models.ImageField(default="try.svg", null=True, blank=True)

