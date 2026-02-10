from django.urls import path
from iplApp import views
#create your urlpatterns here.
urlpatterns = [
    path('', views.home, name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('register-franchise/',views.register_franchise,name='register_franchise'),
]