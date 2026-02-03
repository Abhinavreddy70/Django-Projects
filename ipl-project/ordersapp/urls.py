from django.urls import path
from ordersapp import views

#create your urls here
urlpatterns = [
    path('',views.orders,name='orders')
]