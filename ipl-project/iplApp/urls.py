from django.urls import path
from iplApp import views
#create your urlpatterns here.
urlpatterns = [
    path('', views.home, name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('register-franchise/',views.register_franchise,name='register_franchise'),
    path('franchise-list/',views.franchise_list,name='franchise_list'),
    path('franchise-details/<int:id>/',views.franchise_details,name='franchise_details'),
    path('update-franchise/<int:id>/',views.update_franchise,name='update_franchise'),
    path('delete-franchise/<int:id>/',views.delete_franchise,name='delete_franchise'),
]