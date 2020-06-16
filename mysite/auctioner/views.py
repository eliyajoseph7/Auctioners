from django.shortcuts import render,redirect
from .forms import HouseDetailsForm,CreateUserForm
from .models import HouseDetails
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'auctioner/index.html')




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
def houses(request):
	return render(request, 'auctioner/houses.html')

#Renter Logic here
def renter(request):
	return render(request, 'auctioner/renter.html')

