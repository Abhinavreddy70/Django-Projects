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
    path('register-player/',views.register_player,name='register_player'),
    path('player-list/',views.player_list,name='player_list'),
    path('update-player/<int:id>/',views.update_player,name='update_player'),
    path('delete-player/<int:id>/',views.delete_player,name='delete_player'),
    path('register-stadium/',views.register_stadium,name='register_stadium'),
    path('stadium-list/',views.stadium_list,name='stadium_list'),
    path('update-stadium/<int:id>/',views.update_stadium,name='update_stadium'),
    path('delete-stadium/<int:id>/',views.delete_stadium,name='delete_stadium'),
]