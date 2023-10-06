from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView, RedirectView

from products.views import (
ProductListView, 
ProductDetailView, 
DigitalProductListView, 
ProductIDRedirectView, 
ProductRedirectView,
ProtectedProductDetailView,
ProtectedProductCreateView,
ProtectedProductUpdateView,
ProtectedProductDeleteView,
ProtectedListView
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("about/", TemplateView.as_view(template_name="about.html")),
    path("team/", TemplateView.as_view(template_name="team.html")),
    path("about-us/", RedirectView.as_view(url = "/products/about/")),
    path("products/", ProductListView.as_view(template_name="product_list.html")),
    path("products/<int:pk>/", ProductDetailView.as_view(template_name="product_detail.html")),
    path("digital-products/", DigitalProductListView.as_view()),
    path("products/<slug:slug>/", ProductDetailView.as_view(template_name="product_detail.html")),
    path("p/<int:pk>/", ProductIDRedirectView.as_view()),
    path("p/<slug:slug>/", ProductRedirectView.as_view()),
    #path("my-products/<slug:slug>/", ProtectedProductDetailView.as_view(template_name="product_detail.html")),
    path("my-products/create/", ProtectedProductCreateView.as_view()),
    path("my-products/<slug:slug>/", ProtectedProductUpdateView.as_view()),
    path("my-products/<slug:slug>/delete/", ProtectedProductDeleteView.as_view()),
    path("my-products/",ProtectedListView.as_view())
]
