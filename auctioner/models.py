<<<<<<< HEAD
from django.db import models
from django.contrib.auth.models import User
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




#Customer/renter model
class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)


	def __str__(self):
		return self.name


class House(models.Model):
	street = models.CharField(max_length=120, null=True)
	price = models.DecimalField(max_digits=7, decimal_places=2)
	digital = models.BooleanField(default=False, null= True, blank=True)
	image =models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.street


	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

	


class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete =  models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100,  null=True)

	def __str__(self):
		return str(self.id)

	@property
	def shipping(self):
		shipping = False
		oderitems = self.oderitem_set.all()
		for i in oderitems:
			if i.house.digital == False:
				shipping = True
		return shipping
	


	@property
	def get_cart_total(self):
		oderitems = self.oderitem_set.all()
		total = sum([item.get_total for item in oderitems])
		return total


	@property
	def get_cart_items(self):
		orderitems = self.oderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total
	
	
class OderItem(models.Model):
	house = models.ForeignKey(House, on_delete=models.SET_NULL, null= True, blank= True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)


	@property
	def get_total(self):
		total = self.house.price * self.quantity
		return total
	


class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	order = models. ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
	address = models.CharField(max_length=132, null=False)
	city = models.CharField(max_length=786, null=False)
	state = models.CharField(max_length=254, null=False)
	zipcode = models.CharField(max_length=233, null=False)
	date_added = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.address
||||||| merged common ancestors
=======
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

>>>>>>> 441a40e02279772e92e3a98dc47dca671f506e39
