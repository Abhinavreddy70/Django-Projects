from django.urls import path
from . import views

# Define URL patterns for the store app
urlpatterns = [
    path('products/add/', views.ProductCreateView.as_view(), name='add_product'),
    path('products/',views.ProductListView.as_view(),name='list_product'),
    path('products/<int:pk>/',views.ProductDetailView.as_view(),name='product_details'),
    path('products/<int:pk>/update/',views.ProductUpdateView.as_view(),name='update_product'),
    path('products/<int:pk>/delete/',views.ProductDeleteView.as_view(),name='delete_product'),
    path('reviews/add/', views.ReviewCreateView.as_view(), name='add_review'),
    path('reviews/',views.ReviewListView.as_view(),name='list_reviews'),
    # allow listing reviews for a specific product
    path('products/<int:product_pk>/reviews/', views.ReviewListView.as_view(), name='list_reviews_by_product'),
    path('reviews/<int:pk>/delete/',views.ReviewDeleteView.as_view(),name='delete_review'),
   
]