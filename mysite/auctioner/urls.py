from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('house/', views.houses, name='houses'),
    path('logiin/', views.logiin, name='logiin'),
    path('register/', views.register, name='register'),
    path('houses/', views.house, name='house'),

    path('renter/', views.renter, name='renter')


]