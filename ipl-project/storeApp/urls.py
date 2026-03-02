from django.urls import path
from . import views

# Define URL patterns for the store app
urlpatterns = [
    path('products/add/', views.ProductCreateView.as_view(), name='add_product'),
    path('products/',views.ProductListView.as_view(),name='list_product'),
    path('products/<int:pk>/',views.ProductDetailView.as_view(),name='product_details'),
    path('products/<int:pk>/update/',views.ProductUpdateView.as_view(),name='update_product'),
    path('products/<int:pk>/delete/',views.ProductDeleteView.as_view(),name='delete_product'),
   
]