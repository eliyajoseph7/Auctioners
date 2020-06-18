from django.shortcuts import render,redirect
from django.http import JsonResponse

from .forms import HouseDetailsForm,CreateUserForm
from .models import HouseDetails

from django.contrib import messages


from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users,admin_only

# Create your views here.
def index(request):
    return render(request, 'auctioner/index.html')



#Define Basic home here
def house(request):
    return render(request, 'auctioner/house.html')  



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
@login_required(login_url='index')
@admin_only
def houses(request):
	return render(request, 'auctioner/houses.html')

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
@login_required(login_url='index')
@allowed_users(allowed_roles=['renters'])
def rcart(request):
	return render(request, 'auctioner/rcart.html')

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





#r---means renters
#h---means house owners

