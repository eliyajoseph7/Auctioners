import json
from .models import *



def cookieCart(request):
	try:
		rcart = json.loads(request.COOKIES['rcart'])
	except:
		rcart = { }

	print('rcart:',rcart)
	items = []
	order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
	cartItems = order['get_cart_items']


	for i in rcart:
		try:
			cartItems += rcart[i]['quantity']

			house = House.objects.get(id =i)
			total = (house.price * rcart[i]['quantity'])

			order['get_cart_total'] += total
			order['get_cart_items'] += rcart[i]['quantity']

			item = {
			   'house':{
			       'id':house.id,
			       'street':house.street,
			       'price':house.price,
			       'imageURL':house.imageURL
			   },

			   'quantity': rcart[i]['quantity'],
			   'get_total':total,
			}

			items.append(item)


			if house.digital == False:
				order['shipping'] = True
		except:
			pass 
	return {'cartItems':cartItems, 'order':order, 'items':items}

def cartData(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items =   order.oderitem_set.all()
		cartItems = order.get_cart_items
	else:
		cookieData  = cookieCart(request)
		cartItems = cookieData['cartItems']
		items = cookieData['items']
		order = cookieData['order']
	return {'cartItems':cartItems, 'order':order, 'items':items}



def guestOrder(request, data):

	print('user not logged in')

	print('COOKIES', request.COOKIES)
	name = data['form']['name']
	email = data['form']['email']

	cookieData = cookieCart(request)
	items = cookieData['items']


	customer, created = Customer.objects.get_or_create(
		email=email,
		)
	customer.name = name
	customer.save()

	order = Order.objects.create(
		customer=customer,
		complete=False,
		)

	for item in items:
		house = House.objects.get(id=item['house']['id'])

		oderItem = OderItem.objects.create(
			house = house,
			order = order,
			quantity = item['quantity'])

	return customer, order


