from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product,reviews
from .forms import ProductForm,ReviewForm
# Create your views here.

class ProductCreateView(CreateView):
    model=Product
    form_class=ProductForm
    template_name='add_product.html'
    success_url=reverse_lazy('list_product')


class ProductListView(ListView):
    model=Product
    template_name='list_products.html'
    context_object_name='products'

class ProductDetailView(DetailView):
    model=Product
    template_name='product_detail.html'
    context_object_name='product'

class ProductUpdateView(UpdateView):
    model=Product
    form_class=ProductForm
    template_name='update_product.html'
    # redirect back to listing when update completes
    success_url=reverse_lazy('list_product')

class ProductDeleteView(DeleteView):
    model=Product
    template_name='delete_product.html'
    success_url=reverse_lazy('list_product')
    