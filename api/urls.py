from django.urls import path

from .views import (
    ProductAPIView,
    ProductDetailAPIView
)

urlpatterns = [
    path("", ProductAPIView.as_view(), name="api_list"),
    path("<int:pk>", ProductDetailAPIView.as_view(), name="api_detail")
]
