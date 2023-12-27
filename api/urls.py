from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    ProductAPIView,
    ProductDetailAPIView,
    ProductApiViewSet
)

router = DefaultRouter() 
router.register("api-setview", ProductApiViewSet, basename="api-setview")

urlpatterns = [
    path("", ProductAPIView.as_view(), name="api_list"),
    path("<int:pk>", ProductDetailAPIView.as_view(), name="api_detail"),
    path("", include(router.urls))
]
