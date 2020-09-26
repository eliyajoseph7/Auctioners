var updateBtns = document.getElementsByClassName('update-cart')


for(i = 0; i < updateBtns.length; i++){
	updateBtns[i].addEventListener('click', function(){
		var houseId = this.dataset.house
		var action = this.dataset.action
		console.log('houseId: ',houseId, 'action:', action)

		console.log('USER: ',user)
		if (user == 'AnonymousUser'){
			addCookieItem(houseId, action)
		}else {
			updateUserOrder(houseId, action)

		}

	})
}

function addCookieItem(houseId, action){
	console.log('User is not authenticated..')

	if (action == 'add'){
		if(rcart[houseId] == undefined){
			rcart[houseId] = {'quantity':1}
		}else{
			rcart[houseId]['quantity'] += 1  
		}
	}


	if (action == 'remove'){
		rcart[houseId]['quantity'] -= 1

		if(rcart[houseId]['quantity'] <= 0){
			console.log('item should be deleted')
			delete rcart[houseId];
		}
	}

	console.log('rcart:', rcart)

	document.cookie = 'rcart=' + JSON.stringify(rcart) + ";domain;path=/"
	location.reload()

}


function updateUserOrder(houseId, action){
	console.log('user is authenticated, sending data.....')

	var url = '/update_item/'

	fetch(url, {
		method: 'POST',
		headers:{
			'content-Type': 'application/json',
			'X-CSRFToken':csrftoken,
		},
		body:JSON.stringify({'houseId': houseId, 'action':action})
	})
	.then((response) => {
		return response.json();

	})
	.then((data) => {
		console.log('data:', data)
		location.reload()
	})
}

