from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import(
    ProductAPIView,
    ProductDetailAPIView,
    ProductApiViewSet,
    ProductAPIListView,
    UserProfile
)

router = DefaultRouter() 
router.register("api-setview", ProductApiViewSet, basename="api-setview")

urlpatterns = [
    path("", ProductAPIView.as_view(), name="api_list"),
    path("<int:pk>", ProductDetailAPIView.as_view(), name="api_detail"),
    path("", include(router.urls)),
    path("pagination-view", ProductAPIListView.as_view(), name="pagination_view"),
    path("user-profile/<int:pk>", UserProfile.as_view(), name="user-profile")
]
