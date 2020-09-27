
from django.contrib import admin

# Register your models here.
from .models import *



admin.site.register(Customer)
admin.site.register(HouseDetails)
admin.site.register(House)
admin.site.register(Order)
admin.site.register(OderItem)
admin.site.register(ShippingAddress)
