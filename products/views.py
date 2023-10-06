from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import (
    ListView,
    DetailView,
    RedirectView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Product, DigitalProduct
from .mixins import TemplateTitleMixin
from .forms import ProductModelForm

# Create your views here.
class ProductListView(TemplateTitleMixin, ListView):
    #app_label = "Products"
    #model = Product
    #view_name = list
    #template_name = <app_name>/<model>_<view_name>.html
    #template_name = products/Product_list.html
    model = Product
    title = "Productos"

class ProductDetailView(DetailView):
    model = Product

class DigitalProductListView(TemplateTitleMixin, ListView):
    model = DigitalProduct
    template_name = "product_list.html"
    title = "Productos Digitales"

class ProductIDRedirectView(RedirectView):
     def get_redirect_url(self, *args, **kwargs):
        url_params = self.kwargs
        pk = url_params.get("pk")
        obj = get_object_or_404(Product, pk=pk)
        slug = obj.slug
        return f"/products/products/{slug}"
     
class ProductRedirectView(RedirectView):
     def get_redirect_url(self,*args, **kwargs):
        url_params = self.kwargs
        slug = url_params.get("slug")
        return f"/products/products/{slug}"

class ProtectedProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

class ProtectedProductCreateView(LoginRequiredMixin, CreateView):
    form_class = ProductModelForm
    template_name = "forms.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)

class ProtectedProductUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProductModelForm
    template_name = "product_detail.html"

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
    
    def get_succes_url(self):
        return self.object.get_edit_url()
    
class ProtectedProductDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "forms-delete.html"

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
    
    def get_success_url(self):
        return "/products/products"

class ProtectedListView(LoginRequiredMixin, TemplateTitleMixin, ListView):
    model = Product
    title = "Mis Productos"
    template_name = "product_list.html"

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
    
    def get_succes_url(self):
        return "/products/my-products"
    
