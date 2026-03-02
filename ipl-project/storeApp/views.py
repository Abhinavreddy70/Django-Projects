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



class ReviewCreateView(CreateView):
    model=reviews
    form_class=ReviewForm
    template_name='add_review.html'
    success_url=reverse_lazy('list_reviews')


class ReviewListView(ListView):
    model=reviews
    template_name='list_reviews.html'
    context_object_name='reviews'

    def get_queryset(self):
        # optionally filter by a product passed in the URL
        qs = super().get_queryset()
        self.product = None
        product_pk = self.kwargs.get('product_pk')
        if product_pk is not None:
            # import locally to avoid circular import at top
            from .models import Product
            self.product = Product.objects.filter(pk=product_pk).first()
            if self.product:
                qs = qs.filter(product=self.product)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = getattr(self, 'product', None)
        return context

class ReviewDeleteView(DeleteView):
    model=reviews
    template_name='delete_review.html'
    success_url=reverse_lazy('list_reviews')


