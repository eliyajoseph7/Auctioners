
from django.shortcuts import render,redirect
from django.http import JsonResponse

from .forms import HouseDetailsForm,CreateUserForm
from .models import * 
from .utils import cookieCart, cartData, guestOrder

from django.contrib import messages

from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users,admin_only
import json
import datetime


# Create your views here.
def index(request):
	data  = cartData(request)
	cartItems = data['cartItems']
	
	

	house = House.objects.all()

	context= {'house':house, 'cartItems':cartItems}
	return render(request, 'auctioner/index.html', context)


#Define Basic home here
def house(request):
    return render(request, 'auctioner/house.html')  


def checkout(request): 
	
	data  = cartData(request)
	cartItems = data['cartItems']
	items = data['items']
	order = data['order']
	
	context = {'items':items, 'order':order, 'cartItems':cartItems }
	return render(request, 'auctioner/checkout.html',context)


#Handle login logic here
def logiin(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')


		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request,user)
			return redirect('houses')
		else:
			return redirect('logiin')
	context  = {}
	return render(request, 'auctioner/logiin.html', context)


#Handle register logic here
def register(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			return redirect('logiin')
	context = {'form':form}
	return render(request, 'auctioner/register.html',context)


#House owners logic
def houses(request):
	 
	return render(request, 'auctioner/houses.html')


def house_view(request, id):
	house = House.objects.get(id=id)
	context = {
		'house': house
	}
	return render(request, 'auctioner/theHouse.html', context)

#Renter Logic here
@login_required(login_url='index')
@allowed_users(allowed_roles=['renters'])
def renter(request):
	return render(request, 'auctioner/renter.html')

#house owner setting
@login_required(login_url='index')
@allowed_users(allowed_roles=['admin'])
def hsetting(request):
	return render(request,'auctioner/hsetting.html')



#house owner profile
@login_required(login_url='index')
@allowed_users(allowed_roles=['admin'])
def hprofile(request):
	return render(request, 'auctioner/hprofile.html')


#house owner cart view
@login_required(login_url='index')
@allowed_users(allowed_roles=['admin'])
def  hcart(request):
	return render(request, 'auctioner/hcart.html')


#House owner upload house details
@login_required(login_url='index')
@allowed_users(allowed_roles=['admin'])
def hupload(request):
	return render(request, 'auctioner/hupload.html')


#Renters home page
@login_required(login_url='index')
@allowed_users(allowed_roles=['renters'])
def rindex(request):
	return render(request, 'auctioner/rindex.html')

#Renter see his/her reserved house/room
def rcart(request):

	data  = cartData(request)
	cartItems = data['cartItems']
	items = data['items']
	order = data['order']
	
	context = {'items':items, 'order':order, 'cartItems':cartItems }
	return render(request, 'auctioner/rcart.html', context)

#Renters profile
@login_required(login_url='index')
@allowed_users(allowed_roles=['renters'])
def rprofile(request):
	return render(request, 'auctioner/rprofile.html')


#Renters setting
@login_required(login_url='index')
@allowed_users(allowed_roles=['renters'])
def rsetting(request):
	return render(request, 'auctioner/rsetting.html')



#Admin panel
@login_required(login_url='index')
@admin_only
def s_user(request):#s_user means super user
	return render(request, 'auctioner/s_user.html')


#reset_password template

def reset_password(request):
	return render(request, 'auctioner/reset_password.html')




def updateItem(request):
	data = json.loads(request.body)
	houseId = data['houseId']
	action =data['action']

	print('houseId:',houseId)
	print('action:',action)


	customer = request.user.customer
	house = House.objects.get(id=houseId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	oderItem, created =  OderItem.objects.get_or_create(order=order, house=house)

	if action == 'add':
		oderItem.quantity = (oderItem.quantity + 1)
	elif action == 'remove':
		oderItem.quantity = (oderItem.quantity - 1)
	oderItem.save()


	if oderItem.quantity <= 0:
		oderItem.delete()


	return JsonResponse('item was added', safe=False)

#r---means renters
#h---means house owners



def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)


	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		 

	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id


	if total == order.get_cart_total:
		order.complete = True
	order.save()


	if order.shipping == True:
		ShippingAddress.objects.create(
			customer=customer,
			order=order,
			address=data['shipping']['address'],
			city=data['shipping']['city'],
			state=data['shipping']['state'],
			zipcode=data['shipping']['zipcode'],
			)

	return JsonResponse('Payment complete', safe=False)
