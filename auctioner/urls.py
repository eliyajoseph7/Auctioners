
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('house/', views.houses, name='houses'),
    path('logiin/', views.logiin, name='logiin'),
    path('register/', views.register, name='register'),   
    path('renter/', views.renter, name='renter'),
    path('checkout/', views.checkout, name='checkout'),
    path('house/<int:id>', views.house_view, name='theHouse'),


    #house owner urls
    path('hsetting/', views.hsetting, name='hsetting'),
    path('hprofile/', views.hprofile, name='hprofile'),
    path('hcart/', views.hcart, name='hcart'),
    path('houses/', views.house, name='house'),
    path('hupload/', views.hupload, name='hupload'),


    #Renter urls
    path('rindex/', views.rindex, name='rindex'),
    path('rcart/',views.rcart, name='rcart'),
    path('rprofile/', views.rprofile, name='rprofile'),
    path('rsetting/', views.rsetting, name='rsetting'),
    path('update_item/', views.updateItem, name='updateItem'),
    path('process_order/', views.processOrder, name='processOrder'),


    #Admin urls
    path('s_user/',views.s_user, name='s_user'),


    #reset password
    path('reset_password', views.reset_password, name='reset_password')



]
