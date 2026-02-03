from django.urls import path
from iplApp import views
#create your urlpatterns here.
urlpatterns = [
    path('', views.home, name='home'),
]