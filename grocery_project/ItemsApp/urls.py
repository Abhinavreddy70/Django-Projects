from django.urls import path
from . import views

# Create your urls here.
urlpatterns = [
    path('create', views.create_item, name='create_item'),
    path('list', views.list_items, name='list_items'),
    
]